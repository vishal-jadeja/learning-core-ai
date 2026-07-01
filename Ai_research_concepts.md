# What to Learn Next — Core AI Concept Roadmap

The lesson log (`AI_Learning_Journey.md`) is **complete** — all 12 lessons, the full
arc from "can a machine think?" to today's agents (attention → LLMs → alignment →
agents). That gave the *history and the why.*

This file is the **road ahead**: the core pieces that history **skipped or only
skimmed**, plus the modern topics that postdate the classic arc — the foundation any
AI practitioner/researcher is expected to actually have.

**Scope:** core concepts, not specializations. Keep understanding *how modern AI
works and why each piece exists*, the same first-principles way the lessons ran.
Deep research tracks (interpretability, training infra, novel architectures) come
*after* this foundation is solid.

**Method (unchanged):** one concept at a time — what did the previous step leave
unsolved, what's the idea that fixes it, why does it matter. Understand, then
advance.

Legend: ✅ understood (in the journey) · ⏳ in progress · ⬜ not started

---

## Part A — Gaps inside the LLM stack
*The journey explained the Transformer and LLMs at a concept level but glossed over
several real, load-bearing pieces. Close them.*

### A1. Tokenization (BPE) ⬜
- **Problem:** the journey jumped from words → embeddings, but models actually eat
  **tokens**, not words. What *is* a token?
- **The idea:** subword tokenization (Byte-Pair Encoding) — split text into reusable
  chunks so any word, typo, or language fits a fixed vocabulary.
- **Why it matters:** explains token limits, why models miscount letters, why some
  languages cost more tokens. The layer right before embeddings (Lesson 8).
- **Resource:** Karpathy *Let's build the GPT Tokenizer*.

### A2. Sampling & decoding ⬜
- **Problem:** the model outputs a *probability* over the next token — how do you
  actually pick one? The journey stopped at "predict next token."
- **The idea:** greedy · temperature · top-k · top-p (nucleus) · beam search.
- **Why it matters:** the difference between boring and creative output; the API
  knobs you already tune, now understood from the inside.

### A3. Modern positional encoding & long context ⬜
- **Problem:** Lesson 10 mentioned position "stamps" but used the original 2017
  sinusoidal scheme. Modern models don't.
- **The idea:** **RoPE** (rotary) and friends; how context windows actually stretch
  to 100k–1M tokens, and what breaks at length.
- **Why it matters:** long context is a headline feature of every frontier model.

### A4. The Transformer block, fully ⬜
- **The idea:** the parts Lesson 10 skipped — **residual connections**, **layer
  normalization**, the **feedforward/MLP** sublayer, why each exists.
- **Why it matters:** these are *why* deep Transformers train at all (ties back to
  vanishing gradients, Lesson 7). Needed before building one from scratch.

### A5. Mixture-of-Experts (MoE) ⬜
- **Problem:** scaling laws (Lesson 11) say bigger = better, but every token paying
  for *every* parameter gets ruinously expensive.
- **The idea:** replace the dense MLP sublayer with many **expert** MLPs + a
  **router** that sends each token to only a few → huge total parameter count,
  small *active* compute per token.
- **Why it matters:** how frontier models (GPT-4, DeepSeek, Mixtral, Llama-4) scale
  params without scaling cost-per-token. Now the default, not the exception.

### A6. KV cache & inference cost ⬜
- **Problem:** generating token N re-attends over all previous tokens — recomputing
  their Keys/Values every step is wasteful.
- **The idea:** cache each token's **K** and **V** once, reuse them for every later
  token → the reason generation is fast after the first token.
- **Why it matters:** explains why prompt (prefill) and generation (decode) cost
  differently, why long context eats memory, and prompt-caching pricing. Pairs with
  A2 (sampling).

---

## Part B — Modern alignment & efficiency
*Lesson 11 covered SFT + RLHF. The field moved on; these are the current methods.*

### B1. DPO & RLVR (beyond RLHF) ⬜
- **Problem:** RLHF (Lesson 11) works but is complex and unstable.
- **The idea:** **DPO** (Direct Preference Optimization) skips the separate reward
  model; **RLVR** (RL from *verifiable* rewards) trains on problems with checkable
  answers (math, code).
- **Why it matters:** how current open models are actually aligned; the bridge to
  reasoning models.

### B2. Reasoning & test-time compute ⬜
- **The idea:** spend more compute *while answering* — generate long reasoning
  chains, trained via RL (o1 / R1-style "thinking" models).
- **Why it matters:** the 2025–26 frontier. Why "thinking" models beat bigger
  non-thinking ones on hard tasks; the shift from train-time to test-time scaling.

### B3. Parameter-efficient tuning & quantization ⬜
- **The idea:** adapt or run huge models cheaply — **LoRA**/adapters (train ~1% of
  weights), **quantization** (run in 4/8-bit).
- **Why it matters:** how fine-tuning and local inference are affordable without a
  GPU cluster — directly useful for a builder.

### B4. Prompting & chain-of-thought, properly ⬜
- **The idea:** Lesson 11 noted in-context learning; go deeper — few-shot patterns,
  **chain-of-thought**, why "think step by step" works with *no weight change*.
- **Why it matters:** prompt design is a real lever, not a hack — and it's the
  cheapest one.

---

## Part C — Measuring & systems
*Lesson 12 introduced RAG and agents. Two things remain: learn to* measure*, and
deepen the systems by* building *them.*

### C1. Evaluation — how we measure models ⬜
- **Problem:** with open-ended output, "is it good?" has no easy answer. The journey
  never tackled measurement.
- **The idea:** benchmarks, held-out tests, LLM-as-judge, human eval — and their
  failure modes (contamination, gaming, Goodhart).
- **Why it matters:** **research is measurement.** You can't claim progress you
  can't measure — the most underrated skill on this list.

### C2. RAG & agents — deepen by building 🔁
- **Status:** covered at concept level (Lesson 12) and shipped in production
  already. The gap is *depth through implementation*, not theory.
- **Do:** build a small agent loop (ReAct) and a RAG pipeline from first principles,
  no framework — close the loop on *why* each part works.

### C3. Model Context Protocol (MCP) & tool standards ⬜
- **Problem:** Lesson 12's "harness runs the tool" was hand-wired per tool. How do
  tools get exposed to a model in a *standard* way across apps?
- **The idea:** **MCP** — an open protocol for exposing tools, resources, and prompts
  to any LLM host; the model discovers and calls them uniformly.
- **Why it matters:** the 2025–26 agent-tooling standard, and exactly what Claude
  Code (and this session) runs on. Directly useful for a builder.

---

## Part D — Beyond text (core breadth)
*Two model families every researcher should grasp at a concept level. Neither
appeared in the text-only journey.*

### D1. Multimodal models (vision + language) ⬜
- **The idea:** put images and text in the *same* embedding space (**CLIP**),
  process images as patches-as-tokens (**ViT**), feed both to one model.
- **Why it matters:** how models see; basis of image understanding and modern
  multimodal assistants.

### D2. Diffusion models (image / video generation) ⬜
- **The idea:** generate by reversing a noising process — start from noise, denoise
  step by step into an image.
- **Why it matters:** the *other* giant branch of generative AI (Stable Diffusion,
  Sora). Different math from Transformers — rounds out the picture.

---

## After this foundation — go hands-on, then specialize
The concepts above are the *last* of the reading. The next real step is **building**:

- **Hands-on spine — `AI_RESEARCH_PREP.md`:** build a GPT from scratch → train →
  reproduce a paper. This is where the concepts become real and the portfolio gets
  built.

Then the specialization branches (pick *one* after building):

- **Mechanistic interpretability** — reverse-engineering what's inside the weights.
- **Training & systems** — distributed training, Mixture-of-Experts, kernels.
- **New architectures** — state-space models (Mamba), long-context, efficiency.
- **Safety & alignment research** — the open problems behind Part B.
- **Reading & reproducing papers** — the actual day-to-day of a researcher.

Depth means more when the foundation is wide — so finish A–D, build the GPT, *then*
pick a branch.
