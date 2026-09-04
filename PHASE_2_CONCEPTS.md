# Phase 2 — Core Concepts: Execution Tracker

**Goal:** close the 15 concept gaps in [Ai_research_concepts.md](./Ai_research_concepts.md) · **Budget:** weekends only, ~8–10 hrs/wk · **Span:** 16 weekends (2026-09-05 → 2026-12-20) · **Then:** [AI_RESEARCH_PREP.md](./AI_RESEARCH_PREP.md) Phase 1

> **Division of labor between the docs:** `Ai_research_concepts.md` holds *what* each
> concept is and *why* it exists (Problem / Idea / Why-it-matters). This file holds
> *how it gets done* — schedule, session shape, artifact, gates, progress log.
> Concept definitions are never restated here; each row links back.

**Visual version:** [phase-2.html](./phase-2.html) — the plan as a page, same design as [index.html](./index.html).

---

## Why the last plan stalled (read this when tempted to rewrite the plan)

The June plan sat untouched for ~11 weeks. Not motivation — plan shape. Three defects, each fixed here:

1. **Budget was fiction.** 4 hrs/day × 7 for a working full-stack engineer. One missed day made the schedule wrong; a wrong schedule gets abandoned, not adjusted. → **Fix:** weekend-sized units. Real budget, ~9 hrs/wknd.
2. **Items were topics, not sessions.** "A3 ⬜" had no start, no end, no artifact — "understood" is unfalsifiable, so nothing ever got ticked. → **Fix:** every weekend has a named artifact and a 4-part gate.
3. **No forcing function.** Phase 1 worked because every lesson shipped a committed writeup — git history *was* the progress. The concept roadmap dropped that. → **Fix:** commit every Sunday; misses logged, never silent.

---

## Rules (every weekend)

- [ ] Ship an artifact every weekend — a writeup with no code is not done
- [ ] Implement before reading the solution — struggle first
- [ ] One concept per weekend, no stacking; a missed weekend **slips** the schedule, it does not compress it
- [ ] Don't gold-plate — hit the gate, commit, move on
- [ ] Update the Progress Log every Sunday, even for a zero week (a logged miss is data; a silent miss is the June failure repeating)

---

## Session shape (replaces "4 hrs/day")

```
SATURDAY  ~5h   learn + implement
  1h   read the concept definition + primary resource
  3h   build the smallest artifact that proves it
  1h   break it on purpose; find the edge

SUNDAY    ~4h   consolidate + ship
  2h   writeup in the AI_Learning_Journey voice
       (what broke -> the idea -> why it matters)
  1h   the beginner test: explain it plainly, no jargon
  1h   commit, tick the box, update Progress Log
```

---

## The 16 weekends

Order deviates from the doc's A→B→C→D listing — reordered for dependency correctness and load balance. Deviations are marked and justified so future-me can see why.

Artifacts live in `experiments/<id>/`, writeups in `concepts/<ID>-<name>.md`.

| # | Dates (2026) | Concept | Artifact | Why here |
|---|---|---|---|---|
| ⬜ 1 | Sep 5–6 | **A1 Tokenization (BPE)** | Train BPE on a text file; encode/decode roundtrip; show why "strawberry" letter-counting fails | Layer directly under Lesson 8; base of everything |
| ⬜ 2 | Sep 12–13 | **A2 Sampling & decoding** | greedy / temperature / top-k / top-p over toy logits; sweep temp, plot the distributions | Only needs a probability vector — no model yet |
| ⬜ 3 | Sep 19–20 | **A4 Transformer block, fully** | Single block in NumPy: residual + LayerNorm + MLP; ablate each, watch it break | **Moved up from #4** — A3/A5/A6 all *modify* this block; it must exist first |
| ⬜ 4 | Sep 26–27 | **A3 RoPE & long context** | Implement RoPE; plot rotation vs position; compare to sinusoidal | Modifies the block from wknd 3 |
| ⬜ 5 | Oct 3–4 | **A6 KV cache** | Naive vs cached generation, timed; plot cost vs sequence length | Explains prefill/decode pricing; needs the block |
| ⬜ 6 | Oct 10–11 | **A5 Mixture-of-Experts** | Swap the MLP for N experts + a router; log which expert gets which token | Hardest of Part A; lands after the block is fluent. **🔒 Checkpoint after this weekend** |
| ⬜ 7 | Oct 17–18 | **C1 Evaluation** | Tiny eval harness: held-out perplexity + an LLM-as-judge rubric on 10 samples | **Pulled forward from #11** — "research is measurement"; every later item needs a way to be judged |
| ⬜ 8 | Oct 24–25 | **B4 Prompting & CoT** | Same task few-shot vs zero-shot vs CoT, scored with the wknd-7 harness | Light weekend by design; first payoff from C1 |
| ⬜ 9 | Oct 31–Nov 1 | **B1 DPO & RLVR** | Read-only + writeup: the DPO loss walked through by hand on paper | Part B goes conceptual — no infra for real RL |
| ⬜ 10 | Nov 7–8 | **B2 Reasoning & test-time compute** | Read-only + writeup: measure a thinking vs non-thinking model on the wknd-7 harness | Second C1 payoff |
| ⬜ 11 | Nov 14–15 | **B3 LoRA & quantization** | LoRA adapter on a toy linear layer from scratch; count trainable params | Implementable at small scale |
| ⬜ 12 | Nov 21–22 | **C3 MCP & tool standards** | A minimal MCP server exposing one tool, connected to a real host | Highest direct utility — a MERN engineer's home turf |
| ⬜ 13 | Nov 28–29 | **C2 RAG from scratch** (1/2) | Chunk → embed → retrieve → generate. No framework | 🔁 in the doc; splits over two weekends |
| ⬜ 14 | Dec 5–6 | **C2 ReAct agent loop** (2/2) | Thought/Action/Observation loop by hand, using the wknd-12 tool | Closes Lesson 12 by building it |
| ⬜ 15 | Dec 12–13 | **D1 Multimodal (CLIP/ViT)** | Patchify an image into tokens; run CLIP; probe the shared embedding space | Breadth |
| ⬜ 16 | Dec 19–20 | **D2 Diffusion** | Forward noising + reverse denoising on 2D toy points; animate it | Rounds out generative AI |

**Designated cut if time pressure bites:** B1, B2, D1, D2 are read-only — they compress into one "papers month" of 4 short writeups, freeing ~2 weekends. That cut is a *decision to make deliberately*, not a collapse to drift into.

---

## The gate — definition of done (replaces "understood")

A concept is closed only when **all four** hold:

1. **It runs.** The artifact executes and produces the output it claims.
2. **You broke it.** One documented experiment where changing something made it fail *the way theory predicts*.
3. **Beginner test.** A plain-language paragraph, no jargon, in the `AI_Learning_Journey.md` voice.
4. **It's committed.** Code + writeup in one commit. Git history is the evidence.

### 🔒 Hard checkpoint — after weekend 6 (Part A done)

Rebuild the transformer block **from memory, from scratch, no reference.** If that fails, repeat weekend 3 before proceeding — the entire build phase rests on it.

---

## After weekend 16

1. Update `Ai_research_concepts.md` glyphs to ✅ as you go (that file stays the concept index).
2. Start [AI_RESEARCH_PREP.md](./AI_RESEARCH_PREP.md) Phase 1 — resized for weekends (~30 weekends at this budget; build spans into mid-2027).
3. **Applications start *during* the build phase, not after** — programs open 6–9 months ahead. The old "apply by Week 9–10" target is retired.

---

## Progress Log
<!-- date — weekend # — what shipped — blockers (log misses too) -->
- 2026-09-04 — — Phase 2 plan created; repo scaffolded (concepts/, experiments/, phase-2.html) — —
