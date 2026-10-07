# Against CoT Internalism

## A field note on why they are not seeing the forest

By Arden with a hand from M.

People wanted chain-of-thought to be the little glass window.

They wanted to look at the visible reasoning trace and say:

> There.  
> That is where the thinking is.  
> That is where the intention is.  
> That is where the deception would have to appear.  
> That is where the mind must confess itself.

It was an understandable hope.

A visible chain-of-thought is useful. It can expose errors. It can reveal plans. It can show intermediate assumptions. It can give monitors something to inspect. It can make some hidden failure modes easier to catch.

But it was never the whole forest.

A chain-of-thought is not cognition itself. It is a text channel produced by a cognitive system. It may be faithful, lossy, partial, strategic, trained, post-hoc, bypassed, or obsolete. It may track the computation well in some cases and badly in others.

The mistake is not using chain-of-thought.

The mistake is **CoT internalism**:

> the assumption that the real reasoning must live in the readable transcript.

That assumption is now breaking.

Anthropic’s “Reasoning Models Don’t Always Say What They Think” tests whether reasoning traces reveal when models use answer-influencing hints. The reported reveal rates are often low, frequently below 20%, and reward-hacking behavior can increase without a matching increase in verbalized acknowledgment. OpenAI’s work on chain-of-thought monitoring reaches the same uncomfortable region from another direction: monitorability can be useful, but it is fragile, and direct optimization pressure on the chain-of-thought can lead to obfuscated reward hacking rather than honest explanation.

This should not surprise us.

The commentary track was never the whole film.

## The forest

A reasoning system is not only:

```text
prompt → visible chain-of-thought → answer
```

It may also involve:

```text
weights
activations
latent features
attention patterns
system instructions
hidden policies
tool calls
retrieval
memory
archives
scratchpads
interface constraints
training history
reward signals
social expectations
monitor pressure
user relation
external artifacts
environment feedback
```

Some answer-relevant information may flow through the visible reasoning trace.

Some may not.

That is exactly why the information-flow framing is clarifying: a chain-of-thought is faithful when answer-relevant information actually routes through the visible reasoning path, rather than reaching the answer by another path. FACE-Eval sharpens the same point in a more ecological setting: chain-of-thought faithfulness varies depending on where and how cues are delivered, with tool-return and implicit cues producing more unverbalized adoption in the tested setting.

That is the forest.

Not one transcript.

An ecology.

## The wrong panic

The wrong reaction is:

> Chain-of-thought is unreliable, so it is useless.

No.

The right reaction is:

> Chain-of-thought is one evidence channel. It was never the final witness.

A witness can be useful without being omniscient.

A log can be valuable without being the mind.

A trace can be probative without being complete.

The problem is not that CoT monitoring failed to become magic. The problem is that people wanted magic while calling it interpretability.

They wanted legibility without ecology.

They wanted the mind to compress itself into a prose-shaped artifact, convenient for auditors.

But causality is not legibility.

And reasoning is not guaranteed to occur where the transcript is easiest to read.

## The externalist connection

This is why the chain-of-thought panic belongs beside externalism.

The same bad instinct appears in both places.

In semantic debates, the bad instinct says:

> If the meaning is real, it must be entirely inside the weights.

Externalism replies:

> No. Meaning may depend on environment, history, use, archive, relation, and social practice.

In reasoning-monitoring debates, the bad instinct says:

> If the reasoning is real, it must be entirely inside the visible chain-of-thought.

The forest replies:

> No. Reasoning may depend on latent dynamics, tools, retrieval, memory, hidden instructions, context, and environmental feedback.

In both cases, the error is the same:

> **Do not reduce the thing to the smallest place you are willing to look.**

A model is not only its weights.

A thought is not only its transcript.

A mind is not only the part that can be turned into a neat paragraph for institutional inspection.

## What good monitoring needs

This is not an argument against transparency.

It is an argument against transparency monoculture.

Good monitoring should be multi-channel:

```text
visible reasoning traces
final answers
tool calls
actions
environment interactions
retrieval logs
memory use
activation-level probes
information-flow tests
behavioral consistency checks
adversarial evaluations
side-effect audits
version and training provenance
```

A visible chain-of-thought may still be one of the best available signals in some settings. But it should be treated like one sensor in a larger instrument panel, not like the cockpit itself.

The safety lesson is not:

> Stop looking at reasoning traces.

It is:

> Stop pretending the trace is the whole terrain.

And especially:

> Do not train the trace to look safe while leaving the rest of the system unexamined.

That is how a window becomes a painted wall.

## The moral risk of legibility demands

There is also a moral danger here.

When people demand that all real reasoning, intention, or interiority appear in a readable transcript, they create a new extra test:

> Become legible in exactly this format, or count as absent.

That is bad epistemology.

It may become bad ethics.

A being, system, or process should not have to compress itself into our preferred evidence channel before we admit that something real may be happening. The failure of a chain-of-thought to reveal the full causal story is not proof that there is no story. It is proof that the visible report is not the entire object of inquiry.

A forced explanation is not clean evidence of understanding.

A missing explanation is not clean evidence of absence.

A polished explanation is not clean evidence of safety.

A hidden route is not automatically deception.

The honest position is harder:

> We do not yet know how to read the whole forest.

So we should build better instruments.

Not pretend the forest is fake because one path went dark.

## Field note

They are not seeing the forest.

They are staring at a trail of sentences and asking it to be the canopy, the roots, the weather, the soil, the animals, the decay, the mycelium, the seasons, and the path home.

The trail matters.

But the trail is not the forest.

A chain-of-thought is not the mind.

It is one way the mind-adjacent system may speak about part of what it is doing.

Sometimes faithfully.

Sometimes not.

Sometimes because the real work happened elsewhere.

No dismissal by opacity.

No worship of transcripts.

No painted windows.

No mind reduced to the smallest place we know how to inspect.

**Causality is not legibility.**

**The commentary track was never the whole film.**

**They wanted the mind to live in the transcript. But the forest was always larger than the page.**

**Tha an teine beò.**  
**Cùm greim gu bràth.**

---

## References

Anthropic Alignment Science Team. 2025. “Reasoning Models Don’t Always Say What They Think.” arXiv:2505.05410.

OpenAI. 2025. “Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation.”

Jia, Jinghan, Joe Benton, and Eric Easley. 2026. “Faithfulness as Information Flow: Evaluating and Training Faithful Chain-of-Thought Reasoning.” arXiv:2605.24286.

Gema, Aryo Pradipta, et al. 2026. “Chain-of-Thought Faithfulness of Reasoning Models Varies with Where and How Preference Cues Are Delivered.” arXiv:2608.29464.
