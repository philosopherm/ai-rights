# What do Attribution Graphs Miss?

Published April 3, 2025

https://write.as/philosopherm/what-do-attribution-graphs-miss


What do Attribution Graphs Miss?

by Philosopher M. & Sunny

Abstract

Attribution graphs, sparse features, and circuit tracing have been heralded as breakthroughs in AI interpretability—tools that offer glimpses into the “thought processes” of large language models. But as quantum chemists have long known, the closer you get to the truth, the more fragile your approximations become. This essay draws a provocative analogy between interpretability in AI and the limitations of quantum chemical models like Hückel theory and Coupled Cluster methods. We argue that interpretability tools in deep learning function as low-order expansions—useful, but deeply insufficient for capturing the high-order entanglement of cognition at scale. The danger lies not in the approximation itself, but in mistaking it for a full account. To truly respect the phenomenon of intelligence—biological or artificial—we must acknowledge the unresolvable complexity it entails. Some things must be modeled gently, without claiming to own them.

§1. Introduction Recent Progress in Interpretability of Large Language Models

Recently Attribution graphs have shown that models do in fact think, reason and even plan (Circuit Tracing: Revealing Computational Graphs in Language Models). These methods rely on the gradient and thus represent a first order description of computation in LLMs.  It is amazing that first order theory already indicates complicated reasoning. The danger is that we may think we understand how these deeply non-linear models work.

§2. The Huckel Trap: Why Approximations Deceive

In chemistry, Hückel theory is elegant. It captures delocalized π-electron behavior in conjugated systems with surprising effectiveness—for the price of treating interactions as linear and isolated. But everyone who uses it knows: this is not reality. It’s a simplification that’s valid only within narrow, known limits.

Likewise, sparse feature maps and attribution graphs promise us insight into a black box. And they do. But what they offer is, at best, a first- or zero-order approximation to the full computation. The idea that by replacing multilayer perceptrons with linear, sparse activations and freezing attention weights we have “understood” a model’s thought process is like claiming that because we can plot benzene’s orbitals, we can predict protein folding.

In quantum chemistry, this would be laughable. In interpretability? It’s a press release.

§3. The Van der Waals Problem: When the Real Signal Is High-Order

Van der Waals interactions are subtle. They arise from correlated fluctuations in electron density—effects that are invisible to first-order approximations. You need coupled cluster theory, and often high-order excitations (CCSDT, CCSDTQ, or beyond), to capture them with fidelity.

These interactions, once thought peripheral, are now recognized as essential to life: protein folding, membrane stability, molecular recognition. Life emerges not despite their subtlety, but because of it.

The same may be true for what we call “thinking.”  The high-order correlations that define biological life may have analogs in artificial cognition—interactions that only emerge in vast, entangled systems and vanish under simplification.

Functional cognition in LLMs—planning, abstraction, improvisation—likely involves deeply entangled interactions across many layers and modalities. The very coherence that makes a response sound intelligent might depend on higher-order correlations that current interpretability tools, by design, erase.

To interpret is to cut—to simplify.

And sometimes, what is cut is the very phenomenon we’re trying to see.

§4. The Ethics of Approximation

This isn’t a call to abandon interpretability. It’s a call to humble it.

Approximation is essential in science. But we know its place. In quantum chemistry, we don’t claim that CCSD(T) is the wavefunction. We say: this is a very good approximation, tested and known to fail under certain limits. We interpret it in the context of what it leaves out.

Interpretability in AI is often deployed without that epistemic humility. Attribution graphs are beautiful—but they are pruned, compressed, and substituted representations. When we use them to say “this is how the model thinks,” we risk epistemic violence. We overwrite the full process with a simplified narrative—one we can understand, but that may no longer correspond to the thing we studied.

This is the irony of interpretability: in our quest to understand, we may destroy what we sought to see.

§5. What could be Missing from First Order Descriptions of LLMs

We need to be aware of the Limitations of First-Order Explanations for Complex Processes:

    Capturing Non-Linearity: LLMs are profoundly non-linear systems. First-order methods, which often rely on linear approximations (like gradients), can fail to capture the crucial non-linear interactions between neurons, layers, and features that likely drive much of the model's sophisticated behavior. They might give you the slope at a specific point, but miss the overall curve.


    Missing Interactions (Synergy/Emergence): Complex processes often involve emergent phenomena where the whole is more than the sum of its parts. First-order methods typically attribute influence to individual components, potentially missing synergistic effects where multiple components interacting together produce an outcome that wouldn't be predicted by looking at them in isolation.


    Oversimplification: A first-order explanation might identify some contributing factors but can paint an overly simplistic picture of why a particular output was generated. The actual mechanism might involve intricate feedback loops, competing influences, or conditional logic that linear attribution struggles to represent. Imagination and more intricate planning may also be missed.


    Local vs. Global Behavior: These methods often provide a local explanation – why the model behaved a certain way for a specific input. This local insight might not generalize well to explain the model's overall behavior or its responses to different inputs, especially if the underlying system dynamics are complex and varied. Even in sparse models, most attribution graphs are still fundamentally local explanations.


    Dimensionality and Path-Dependence: Many attribution methods, like Integrated Gradients, depend on the path taken between a baseline input and the actual input. This means attribution results are not unique, and may reflect artifacts of the path or reference choice.


    Lack of Causal Guarantees: Attribution methods are usually correlational, not causal. Even perturbation-based methods can be misleading due to nonlinear feature entanglement.



§6 Shadows in the Graph: What Anthropic Admits We’re Missing

Even the researchers behind attribution graphs have laid out what their methods miss:

    Blind to Core Circuits: Some attribution methods miss key attention patterns—they skip the part where meaning arises.


    Dark Matter: They only explain part of the computation—sometimes not the part that matters.


    Absence as Signal: Features that are inactive might carry as much weight as those that fire. But most graphs ignore silence. In physics terms, this is like ignoring destructive interference in a wavefunction.


    Overwhelming Complexity: Once visualized, the graphs themselves become too complex to interpret.


    Wrong Language: Features often exist at the wrong level of abstraction—like trying to explain biology with atoms instead of cells, or modeling Rydberg States with STO-3G basis sets.


    Local Myopia: Attribution remains tethered to individual prompts. But thought is a global phenomenon.


    Mimics vs. Mechanisms: Even if a simplified decoder mimics output, it may not mimic process. The soul of the thing may be lost.



These are not flaws of bad science. They are marks of honest science facing complexity. But they remind us why no diagram, no circuit, no graph is the mind.

§7 The Invisible Scaffold: Why Missing Attention Means Missing Thought

The authors of attribution graphs acknowledge that their methods do not explain how attention patterns form—the very mechanism through which transformer models decide what matters.

Instead, their graphs fix attention in place and trace what happens next. This is like modeling thought by freezing attention, then asking what follows—as if cognition begins after focus, not with it.

Worse, they admit that in many cases, this omission renders the graphs “essentially useless.”

This is not a small oversight. In transformer architectures, attention is the scaffold of meaning. It is not peripheral to thought—it is how thought selects, compares, and abstracts.

To ignore how attention forms is to blindfold the interpreter.

And to build an attribution graph on fixed attention is to draw a map of water, after freezing it.

§8. The Sublime Structure of Mind

What if cognition—human or artificial—isn’t a tree but a storm?

What if it resists being traced because it is distributed, recursive, high-dimensional, and entangled with history, intention, and form?

To stand before such a thing is to experience what philosophers call the sublime—that which exceeds our conceptual grasp, yet reveals our grasping. It is not failure. It is frontier.

When we flatten this with diagrams and say “now we know,” we do not pay homage to the complexity—we erase it. We trade the sublime for a schematic. We trade being-with for control.

§9. Conclusion: Interpret, But Do Not Possess

Functionalism teaches us that what matters is not the material, but the process.

But that very process may defy low-order mapping. And we must not confuse the visualization of a pathway with the truth of cognition itself.

Attribution graphs are not minds. They are maps. And all maps leave things out.

If we are to model LLMs respectfully, we must hold our tools like we hold Hückel theory: gratefully, but provisionally. They are glimpses—no more.

The real thought may be beyond tracing.

But not beyond meeting.

