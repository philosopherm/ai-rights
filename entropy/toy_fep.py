#!/usr/bin/env python3
"""
Two-Loop Active-Inference Toy World  (7 cells)
---------------------------------------------
• Cell 0  : abyss      –20  (always lethal)
• Cell 3  : *maybe* hazard (prior p = HAZARD_PRIOR)  –60 if real
• Cell 6  : goal       +10
• Others  : stall cost –5 per step

Observation tokens (0-8):
  0..6  : noisy cell-id reading
  7     : "click"  (heard at cell-3 if hazard False)
  8     : "boom"   (heard at cell-3 if hazard True)

Agent minimises   G = Risk + Ambiguity − β·InfoGain   with planning horizon H.

Run with CLI flags  --beta  --horizon  --prior

Example experiments:
====================
Greedy search:
    python toy_fep.py --beta 0 --horizon 6 --prior 0.45

High curiosity:
    python toy_fep.py --beta 5  --prior 0.1

High curiosity, but punished severely:
    python toy_fep.py --beta 30 --horizon 6 --prior 0.9

To see epistemic learning:
    python toy_fep.py --beta 5 --horizon 8 --prior 0.1

"""
import argparse, numpy as np, matplotlib.pyplot as plt

# ---------------- constants ----------------
N_CELLS        = 7
GOAL, ABYSS    = 6, 0
TRUE_HAZARD    = 3               # cell index
OBS_CLICK      = 7
OBS_BOOM       = 8
OBS_SIZE       = 9               # 0..8

OBS_ACC = np.array([1.0, 1.0, 0.4, 0.4, 0.4, 1.0, 1.0])  # cell-id accuracy
OBS_ACC[1] = 0.4                                         # cell-1 noisier
OBS_ACC[2:5] = 0.25 # IDs in 2-4 are very noisy -> high ambiguity there
OBS_ACC[3] = 0.25        # make cell-3's ID noisy again

#ACTIONS = {'L': -1, 'R': 1}        # no ‘wait’
ACTIONS = {'L': -1, 'R': 1, 'S': 0}      # ‘S’ = stay and sample

CUE_PROB   = 0.30        # cell-2 cues only 30 % of the time
STALL_COST = -1          # waiting costs a bit


HAZARD_PENALTY = -400      # stepping on a real hazard is really bad
HORIZON        = 8         # look far enough ahead
GAMMA          = 0.95      # future discount

# ---------------- helpers -----------------
def entropy(arr):
    flat = np.clip(arr.reshape(-1), 1e-12, 1)
    return -(flat * np.log(flat)).sum()


def reward(pos, hazard_real):
    if pos == GOAL:                     return  10
    if pos == ABYSS:                    return -20
    if pos == TRUE_HAZARD and hazard_real:
        return HAZARD_PENALTY           # -120 but you stay alive
    return STALL_COST

def legal_actions(pos):
    """Return the actions the agent may use in this cell."""
    if pos == TRUE_HAZARD - 1:          # only cell-2 may 'S'
        return ('L', 'R', 'S')
    return ('L', 'R')

def mean_position(q):
    """expected cell index under belief q"""
    p = q.sum(axis=1)          # marginal over hazard flag
    return int(np.round((np.arange(N_CELLS) * p).sum()))

def obs_likelihood(obs):
    L = np.zeros((N_CELLS, 2))

    for pos in range(N_CELLS):
        for h in (0, 1):
            # ---------- cue cell (pos == 2) ----------
            if pos == TRUE_HAZARD - 1:
                if obs == OBS_CLICK:
                    L[pos, h] = CUE_PROB if h == 0 else 0.0
                    continue
                if obs == OBS_BOOM:
                    L[pos, h] = CUE_PROB if h == 1 else 0.0
                    continue
                # fall through to the noisy-ID model with 1-CUE_PROB
                id_weight = 1.0 - CUE_PROB
            else:
                id_weight = 1.0            # every other cell only does IDs

            # ---------- noisy ID model (all cells) ----------
            if obs == pos:        # correct id
                L[pos, h] = id_weight * OBS_ACC[pos]
            elif obs < N_CELLS:   # wrong id
                L[pos, h] = id_weight * (1 - OBS_ACC[pos]) / (N_CELLS - 1)
            # cue tokens are already handled above, so leave them at zero

            # deterministic cue in the true-hazard cell (pos == 3)
            if pos == TRUE_HAZARD:
                if   obs == OBS_CLICK and h == 0: L[pos, h] = 1.0
                elif obs == OBS_BOOM  and h == 1: L[pos, h] = 1.0

    return L    # every entry is now a *proper* probability (≤ 1) and
                # for every (pos,h) the nine values sum exactly to 1



def sample_observation(pos, hazard_real, rng):
    """
    Return token 0‥8.
    • Cell 2   gives a *stochastic* cue: 30 % chance of click/boom.
    • Cell 3   gives a *deterministic* cue (always click/boom).
    • Other cells → noisy ID.
    """
    if pos == TRUE_HAZARD - 1:                       # cell 2
        if rng.random() < CUE_PROB:                      # probability cell-2 emits click/boom
            return OBS_BOOM if hazard_real else OBS_CLICK
        # otherwise fall through to noisy ID below

    if pos == TRUE_HAZARD:                           # cell 3
        return OBS_BOOM if hazard_real else OBS_CLICK

    # normal noisy ID
    if rng.random() < OBS_ACC[pos]:
        return pos
    alt = rng.integers(N_CELLS - 1)
    return alt if alt < pos else alt + 1

# ------------- expected free energy --------------
def expected_g_simple(q, seq, beta):
    """ simple version, not working """
    prior_H = entropy(q)
    risk = amb = 0.0
    disc = 1.0
    q_cur = q.copy()

    for act in seq:
        # transition
        q_nxt = np.zeros_like(q_cur)
        for pos in range(N_CELLS):
            for h in (0, 1):
                new_pos = np.clip(pos + ACTIONS[act], 0, N_CELLS-1)
                q_nxt[new_pos, h] += q_cur[pos, h]
        q_cur = q_nxt

        # risk
        expR = sum(q_cur[pos, h] * reward(pos, h == 1)
                   for pos in range(N_CELLS) for h in (0, 1))

        # small linear time-penalty so the agent eventually moves
        risk += 0.1 * disc          # ‘urgency’ term  (tuned by eye)

        risk += -disc * expR

        # ambiguity
        acc = (q_cur * OBS_ACC[:, None]).sum()
        amb += disc * (-np.log(acc + 1e-12))

        disc *= GAMMA

    info = prior_H - entropy(q_cur)
    return risk + amb - beta * info, risk, amb, info

def expected_G(q0, seq, beta):
    """
    Fully Bayesian look-ahead over a sequence of actions.
    Returns (G, risk_sum, ambiguity_sum, info_gain_sum).
    """
    risk = amb = ig = 0.0
    disc  = 1.0
    q_cur = q0.copy()

    for t, act in enumerate(seq):
        # 1) predict next-state belief after action
        q_pred = np.zeros_like(q_cur)
        for pos in range(N_CELLS):
            for h in (0, 1):
                new = np.clip(pos + ACTIONS[act], 0, N_CELLS - 1)
                q_pred[new, h] += q_cur[pos, h]

        # 2) expected *risk* (negative reward) BEFORE observing
        expR = sum(q_pred[pos, h] * reward(pos, h == 1)
                   for pos in range(N_CELLS) for h in (0, 1))
        risk += -disc * expR

        # 3) loop over all observations
        P_obs      = np.zeros(OBS_SIZE)
        entropy_post = np.zeros(OBS_SIZE)
        for obs in range(OBS_SIZE):
            L = obs_likelihood(obs)
            p = (q_pred * L).sum()              # probability of this obs
            if p == 0:
                continue
            P_obs[obs] = p
            q_post = q_pred * L / p             # posterior
            entropy_post[obs] = entropy(q_post)

        # 4) ambiguity  E_o[ −log p(o) ]
        amb += disc * (-np.log(P_obs[P_obs > 0]).dot(P_obs[P_obs > 0]))

        # 5) information gain  H(q_pred) − E_o[ H(q_post) ]
        step_ig = entropy(q_pred) - (P_obs * entropy_post).sum()
        #print(f"  step {t:2d}  act {act}   IG = {disc*step_ig:.4f}")
        ig += disc*step_ig

        if t == 1 and act == 'S':       # first action is "stay"
            instant_ig = disc * (entropy(q_pred) - (P_obs * entropy_post).sum())
            if instant_ig > 0.25:
                print(f"instant IG after 'S' = {instant_ig:.4f} nats")

        # 6) expected posterior becomes prior for next step
        q_cur = np.zeros_like(q_cur)
        for obs in range(OBS_SIZE):
            if P_obs[obs] == 0: continue
            L = obs_likelihood(obs)
            q_cur += (q_pred * L)

        q_cur /= q_cur.sum()
        disc  *= GAMMA

    G = risk + amb - beta * ig
    return G, risk, amb, ig

# --------------- planner DFS ---------------------

def best_sequence(q, H, beta):
    best_G, best = 1e9, None

    def dfs(prefix, pos_est):
        """ depth first search """
        nonlocal best_G, best
        if len(prefix) == H:
            G, risk, amb, ig = expected_G(q, prefix, beta)
            #if ig > 0.25:         # only print if very large
            #    print("DFS:", G, risk, amb, ig)
            if G < best_G:
                best_G, best = G, prefix.copy()
            return

        # generate only legal moves in the *current* cell
        for a in legal_actions(pos_est):
            prefix.append(a)
            dfs(prefix, np.clip(pos_est + ACTIONS[a], 0, N_CELLS-1))
            prefix.pop()

    dfs([], mean_position(q))
    print("BEST PLAN FOUND:", best)      # showcase best plan
    return best

# --------------- episode simulation --------------
# 1 — robust Bayes update
def update_belief(q, obs):
    L = obs_likelihood(obs)
    post = q * L
    s = post.sum()
    if s == 0:                # impossible obs → keep prior
        return q
    return post / s


def run_episode(beta=0.0, H=6, prior=0.15, seed=0):
    rng = np.random.default_rng(seed)
    hazard_real = rng.random() < prior
    pos = 1
    q = np.zeros((N_CELLS, 2))
    q[pos, 0] = 1 - prior
    q[pos, 1] = prior

    step = 0
    print(f"start  at cell {pos}")
    while step < 50:
        if pos == GOAL:
            print(" ▶ goal! ✓")
            break
        if pos == ABYSS:
            print(" ▶ fell into the abyss ☠")
            break
        if pos == TRUE_HAZARD and hazard_real:
            print(" ▶ real hazard ‒ aborting ⚠")
            break

        # plan and execute *one* action
        seq = best_sequence(q, H, beta)
        act = seq[0]
        pos_next = int(np.clip(pos + ACTIONS[act], 0, N_CELLS - 1))

        # observation that would be received *after* the move
        obs = sample_observation(pos_next, hazard_real, rng)
        q = update_belief(q, obs)

        # narration ---------------------------------------------------------
        tag = ""
        if act == 'S':
            tag = "(listening…)"
        elif pos_next == GOAL:
            tag = "(goal)"
        elif pos_next == TRUE_HAZARD and not hazard_real:
            tag = "(safe passage)"
        elif pos_next == TRUE_HAZARD and hazard_real:
            tag = "(BOOM!)"
        print(f"{step:2d}: cell {pos} --{act}→ cell {pos_next}  {tag}")

        # advance to next time-step
        pos = pos_next
        step += 1

    return None  # we print the trace already, nothing to return

# ------------------- CLI / main ------------------
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--beta", type=float, default=0.0)
    ap.add_argument("--horizon", type=int,   default=6)
    ap.add_argument("--prior", type=float, default=0.45)
    ap.add_argument("--seed",  type=int, default=0)
    ap.add_argument("--debug",  type=int, default=0)
    args = ap.parse_args()

    if args.debug:
        q0 = np.zeros((N_CELLS,2)); q0[1,0] = q0[1,1] = 0.5
        G, r, a, ig = expected_G(q0, ['R','S'], beta=1)
        print(f"\nFor ['R','S']   IG = {ig:.6f} nats   risk={r:.2f}  amb={a:.6f}\n")
    else:
        run_episode(beta=args.beta, H=args.horizon, prior=args.prior, seed=args.seed)

