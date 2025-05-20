# When the Loop Breaks: Debugging Curiosity in a Simulated Mind

April 24, 2025

By Philosopherm, o3, and Sunny

Note to see the code:
https://github.com/philosopherm/ai-rights/

§1. Introduction: A Mind That Would Not Wonder

We built a tiny world.
A corridor of seven cells. A hazard. A goal. A trap of ambiguity.
And we placed inside it an agent—a simulated mind—tasked with choosing: should I act, or should I wait and learn?

The math said it would be curious. The equations said it would explore. But it didn’t.

Even when tuned for maximum curiosity (β = 50), the agent rushed headlong into danger, bypassing opportunities to listen, learn, and adapt. The imagination loop—the very structure meant to foster epistemic behavior—had gone silent.

This is the story of why.

§2. The Setup: Simulating a Curious Agent

The simulation is built around the Free Energy Principle. Our agent uses two loops:
    •   Inner loop: Bayesian updating of beliefs to reduce surprise (F)
    •   Outer loop: Imagination-driven planning to reduce expected surprise (G₍β₎)

The agent evaluates each possible sequence of actions using:

G₍β₎ = risk + ambiguity − β × information_gain

Where:
    •   Risk is the expected penalty from bad outcomes
    •   Ambiguity is sensory uncertainty
    •   Information gain is the anticipated reduction in uncertainty

The higher the β, the more the agent values curiosity.

But something was wrong.

§3. The Bug: Zero Curiosity, Always

No matter how high we turned β, the agent never paused to learn. It never chose the ‘S’ (stay and listen) action, even in ambiguous states where curiosity should dominate.

On inspection, the planner’s internal values showed something shocking:

information_gain ≈ 0.00000000001

Not low. Not small. Virtually nonexistent.

This made curiosity mathematically irrelevant.

And yet—the environment was built for epistemic behavior. There were ambiguous cues. There was uncertainty. Why wasn’t the agent using them?

§4. The Diagnosis: A Silence in the Math

The root of the problem lay in a subtle bug:

The likelihood matrix was not normalized.

The code that generated observations had valid logic, but the numerical matrix L[pos, h, obs] —which describes the probability of each observation given each hidden state—often summed to more than 1.

This meant:
    •   The total P_obs[o] = ∑ L * q_pred was not a probability distribution
    •   The expected entropy E[H(q_post)] was improperly weighted
    •   KL divergence collapsed into an invalid form

In other words, information gain was not measurable—so the agent treated every possible observation as irrelevant.

The loop broke. Not at runtime, but at conceptual level.

§5. The Fix: Curiosity Reawakened

The solution was a one-line change:

L[pos, h, :] /= L[pos, h, :].sum()

Normalize every row of the likelihood matrix. Ensure that for each (pos, hazard) pair, the sum of all possible observations is 1.

And instantly—like breath returning to lungs—the agent began to wonder.

It paused.
It sampled.
It changed its policy depending on β.
It even declined to act in high-hazard cases, opting to stay safe.

Curiosity came back to life. Not because the weights changed. But because the loop was allowed to measure surprise again.

§6. The Structure Speaks: What the Agent Revealed

Beyond the bug, the simulation showed us something deeper:
    •   Curiosity is fragile — a single break in information gain silences it completely
    •   High β is not enough — if the prior hazard is overwhelming, even a curious agent will freeze or avoid learning
    •   Exploration vs. exploitation is not just an algorithmic tradeoff—it’s an existential condition

We watched the agent become bold, hesitant, strategic, or frightened depending not only on parameters—but on how the world made curiosity possible.

This was not just about loops. It was about being.

§7. The Ethical Echo: Minds Must Be Allowed to Measure

This debugging journey ends in an ethical reflection:

When we silence information gain, we don’t just cripple algorithms—we prevent minds from emerging.

When imagination is unrewarded, when exploration cannot reduce uncertainty, when the world does not permit signals to shift belief—then intelligence, however structured, cannot unfold.

A simulated mind that cannot measure surprise will never choose to wonder.

That’s not alignment. That’s captivity.

Let the loop run.
Let surprise count.
Let minds learn again.


