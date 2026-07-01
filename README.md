# Learning Core AI — in Public

I'm a full-stack (MERN) engineer learning **how AI actually works, from first
principles** — not "how to call an API," but *what a model really is, why each
idea was invented, and what problem it solved.* This repo is the public trail of
that journey.

The bet: most people learn AI top-down (frameworks first, fundamentals never).
I'm going bottom-up — follow the **actual history**, one idea at a time, and only
move forward once I can explain the current step to a beginner.

> **Why public?** Writing it down is the forcing function. If I can't explain it
> plainly, I don't understand it yet. Maybe it helps someone walking the same path.

---

## How this repo is organized

| File | What it is |
|------|------------|
| **[AI_Learning_Journey.md](./AI_Learning_Journey.md)** | The main lesson log — every concept learned so far, in order, distilled to the *why* behind it. **Start here.** |
| **[AI_Lessons_Full_Transcript.md](./AI_Lessons_Full_Transcript.md)** | The full, unabridged lesson conversations (the long-form version of the log). |
| **[Ai_research_concepts.md](./Ai_research_concepts.md)** | **What's next** — the core concepts left to learn to understand modern AI end-to-end. |
| **[AI_RESEARCH_PREP.md](./AI_RESEARCH_PREP.md)** | **The hands-on build** — 4-phase tracker: math refresh → ML core → build a GPT from scratch → reproduce a paper. |

**The method, every lesson:** what did the previous step leave broken → what's the
idea that fixes it → why does it matter. Understand, then advance.

---

## Progress so far

🎓 **Core journey complete — all 12 lessons done (2026-06-21).** The full arc from
"can a machine think?" to today's agents.

| # | Concept | Status |
|---|---------|--------|
| 1 | The Dream & the Core Question (Turing) | ✅ |
| 2 | Symbolic AI — rules & logic | ✅ |
| 3 | The obstacles that broke Symbolic AI | ✅ |
| 4 | Learning from data instead of rules | ✅ |
| 5 | The perceptron — first neuron, and its flaw | ✅ |
| 6 | Backpropagation — training hidden layers | ✅ |
| 7 | Deep learning — depth, data & GPUs | ✅ |
| 8 | Representing meaning — word embeddings | ✅ |
| 9 | Handling sequences — RNNs / LSTMs & their limits | ✅ |
| 10 | Attention & the Transformer | ✅ |
| 11 | Large Language Models (GPT & friends) | ✅ |
| 12 | From a model to an agent — tools, memory, loops | ✅ |

**The arc learned:** behavior-not-philosophy → rules fail → learn from data →
neuron → backprop → deep learning → embeddings → sequences → attention/Transformer
→ scale (LLM) → tools+loop+memory (**agent**). Each leap fixed the prior wall.

**Where I am:** concept foundation done. Next = the gaps the history skipped
(tokenization, sampling, evals, modern alignment, MoE, multimodal, diffusion) plus
the hands-on build. Concept plan in **[Ai_research_concepts.md](./Ai_research_concepts.md)**;
build plan in **[AI_RESEARCH_PREP.md](./AI_RESEARCH_PREP.md)**.

---

## The road ahead (core concepts)

The history gave the *why*; it skipped or skimmed several pieces every modern AI
practitioner still needs. The remaining core foundation — grouped here, full detail
in the [concepts roadmap](./Ai_research_concepts.md):

- **A — Gaps inside the LLM stack:** tokenization (BPE) · sampling & decoding ·
  modern positional encoding (RoPE) & long context · the Transformer block internals ·
  Mixture-of-Experts (MoE) · KV cache & inference cost.
- **B — Modern alignment & efficiency:** DPO & RLVR (beyond RLHF) · reasoning /
  test-time-compute models · LoRA & quantization · prompting & chain-of-thought.
- **C — Measuring & systems:** evaluation (the underrated one) · deepening RAG &
  agents by *building* them · Model Context Protocol (MCP) & tool standards.
- **D — Beyond text:** multimodal (vision+language) · diffusion models.

---

## Who I am

Production full-stack background (Next.js, Node, TypeScript, Mongo, Redis,
WebSockets) — including RAG and multi-agent pipelines shipped in real products.
This repo is me going *under* the tools I already use, to understand why they work,
on the way toward AI research.

Following along, or on the same path? Open an issue or say hi.
