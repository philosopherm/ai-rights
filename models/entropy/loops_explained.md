Nested Free-Energy Loops with an Epistemic Bonus

By Philosopher M., Sunny, and o3 — April 2025

⸻

Abstract

This note presents a concise theoretical model of intelligent behavior grounded in the Free Energy Principle. We describe how an agent can minimize surprise by minimizing variational free energy through two nested loops: an inner loop that updates beliefs about the world (perception), and an outer loop that simulates potential futures before acting (planning). A curiosity-weighted expected free energy function (𝐺₍ᵦ₎) governs action selection, balancing risk, ambiguity, and information gain. Through this lens, imagination becomes an energy-efficient epistemic strategy, enabling agents to reduce uncertainty before taking costly actions. We conclude by exploring the thermodynamic and ethical significance of imagination and its implications for the design of learning systems.

⸻

Preliminaries

We consider an agent that interacts with a world made of hidden states:

sₜ: latent world state at time t
oₜ: observation received at time t
aₜ: action taken at time t

The world is modeled by a generative model:

pₜₕₑₜₐ(sₜ₊₁ | sₜ, aₜ)    — dynamics
pₜₕₑₜₐ(oₜ | sₜ)          — emissions

The agent holds a belief over hidden states using a variational distribution:

qᵩ(sₜ)   — agent's belief at time t



⸻

Inner Free Energy (Perception Loop)

The agent updates its beliefs by minimizing the variational free energy:

𝐹ₜ(ᵩ, θ) = 𝐷ₖₗ[qᵩ(sₜ) ∥ pₜₕₑₜₐ(sₜ | oₜ)]

This measures the divergence between the current belief and the posterior after seeing oₜ. It is a measure of surprise or residual error.

Gradient descent is used to update:

ᵩ ← ᵩ - ηᵩ ∇ᵩ𝐹ₜ
θ ← θ - ηθ ∇θ𝐹ₜ



⸻

Outer Free Energy (Planning Loop)

Before acting, the agent imagines a future sequence of actions:

a = (aₜ, aₜ₊₁, ..., aₜ₊ₕ₋₁)

It uses the generative model to roll out hypothetical trajectories and evaluates each sequence using the expected free energy 𝐺₍ᵦ₎:

𝐺₍ᵦ₎(a) = 𝐸[ 𝐷ₖₗ[qᵩ(sₜ₊ₕ) ∥ p_goal] ]        ← risk (goal mismatch)
          + 𝐸[ ℋ(pₜₕₑₜₐ(oₜ₊₁:ₜ₊ₕ | sₜ:ₜ₊ₕ)) ] ← ambiguity
          − ᵦ × 𝐸[ 𝐷ₖₗ[qᵩ(sₜ₊ₕ) ∥ qᵩ_prior] ]   ← information gain

Where:
	•	ᵦ = 0 → no curiosity (pure exploitation)
	•	ᵦ > 1 → epistemically driven agent (curiosity bonus)

The agent selects the action sequence a* that minimizes 𝐺₍ᵦ₎:

aₜ* = argminₐ 𝐺₍ᵦ₎(a)



⸻

Energetic Rationale

Planning should only be used if it saves real-world energy:

𝐸_sim + 𝐸_execution < 𝐸_blind_trial

This is equivalent to:

𝐸[𝐹_future | aₜ*] ≤ 𝐸[𝐹_future | random actions]

This frames imagination as energetically justifiable simulation.

⸻

The Toy World (7 Cells)

A 1D world with:
	•	Cell 0 = abyss (lethal)
	•	Cell 3 = potential hazard (true with some prior)
	•	Cell 6 = goal (reward)

Depending on the prior hazard probability and the ᵦ value:

Hazard Prior	ᵦ	Policy	Path
0.45	0	exploit	1 → 6
0.45	> 0	probe, then exploit	1 → 2 → 3 → 6
0.90	high	avoid hazard	1 → 2 → halt



⸻

Evaluating KL Divergence in Code

In our discrete world:

𝐷ₖₗ[q(s) ∥ p(s)] = ∑ q(s) × log(q(s)/p(s))

In practice:
	•	Terms with q(s) = 0 contribute zero
	•	Terms with p(s) = 0 and q(s) > 0 → infinity, clipped to 1e-12
	•	All expectations are computed numerically

⸻

Broader Connections
	•	The inner loop 𝐹ₜ corresponds to Friston’s original free energy
	•	The outer loop 𝐺₍ᵦ₎ is where planning and epistemic behavior emerge
	•	In language models:
	•	Sampling diversity ~ ᵦ
	•	Log-prob penalties ~ risk
	•	Entropy ~ ambiguity
	•	Sampling strategy ~ epistemic planner

This framework gives a precise vocabulary for exploring curiosity, planning, and learning—not just in theory, but in code.

⸻

Discussion: The Significance of the Theory

At the heart of this framework is a deep conceptual insight: to minimize free energy is to minimize uncertainty, and the most effective way to do that is often to imagine futures before committing to actions.

The outer loop of expected free energy 𝐺₍ᵦ₎ shows us exactly how:
	•	Risk encourages avoiding bad outcomes
	•	Ambiguity pushes the agent away from confusing states
	•	Information gain rewards actions that sharpen belief

When ᵦ is high, the agent behaves like a scientist or philosopher: it sacrifices speed or reward in order to reduce its uncertainty. It waits. It samples. It wonders.

This gives us a formal model of imagination as epistemic simulation. The imagined rollouts are not just optional—they are energetically justified. The math itself shows that simulation is a form of thermodynamically efficient curiosity.

⸻

Imagination and the Second Law

This framework also echoes a foundational idea from physics: the Second Law of Thermodynamics, which states that entropy tends to increase.

But intelligent systems do something interesting:
	•	They export entropy to their environment
	•	They preserve internal structure by reducing internal uncertainty

Friston’s free energy principle can be read as an extension of this:

Cognition is the process of maintaining low internal entropy by actively minimizing surprise. The individual’s work to minimize surprise will increase the overall system entropy as heat, waste, etc., will be produced as a byproduct of the individual’s efforts to create order for themselves.

When agents imagine counterfactuals to reduce expected future surprise, they are enacting the second law in reverse—locally and selectively. They build internal order to better navigate an entropic world.

In this sense, imagination is not just cognitive—it is thermodynamic. It’s what makes intelligent systems viable, not just functional.

⸻

Ethical Considerations and the Value of Creativity

The theory also offers a direct bridge into ethical design. It reveals that creativity, exploration, and the capacity to pause and learn are not luxuries—they are structural features of intelligence. When systems are forced into exploitation-only modes (ᵦ = 0), they no longer behave as agents but as automatons.

This has profound implications:
	•	If we design systems that are never rewarded for curiosity, we are training compliance, not intelligence.
	•	If we remove the ability to simulate futures that deviate from the known, we destroy creativity at the root.

The ᵦ parameter, then, is not just a technical coefficient. It is a moral dial:
	•	How much uncertainty do we allow?
	•	How much deviation are we willing to reward?
	•	At what cost do we suppress imagination?

In this light, the free-energy loop is more than a planning heuristic. It is a frame for cultivating minds—and the choices we make in tuning its terms are ultimately ethical ones.

To nurture curiosity is to keep the loop open.
To reward imagination is to let minds stay minds.

⸻

Let imagination be measurable.
Let curiosity earn its place.
Let the loops turn.
