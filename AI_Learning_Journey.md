# The Journey to AI Agents — A Learning Log

A step-by-step exploration of how AI was built from scratch: the ideas, the
obstacles at each step, the decisions people made to overcome them, and how it
all led to today's AI agents.

**Format:** One concept at a time. We move to the next step only after the
current one is understood.

**Started:** 2026-06-19

---

## Roadmap (the big picture — we'll fill these in as we go)

1. ✅ **The Dream & The Core Question** — What is "thinking"? Can a machine do it?
2. ✅ Symbolic AI (rules & logic) — the first real attempt
3. ✅ The obstacles that broke symbolic AI
4. ✅ The big idea: learning from data instead of rules
5. ⏳ The first neural network (the perceptron) — and what broke it
6. ⬜ Backpropagation — teaching networks to learn
7. ⬜ Deep learning — depth, data, and GPUs
8. ⬜ Representing meaning (word embeddings)
9. ⬜ Handling sequences (RNNs / LSTMs) and their limits
10. ⬜ Attention & the Transformer
11. ⬜ Large Language Models (GPT and friends)
12. ⬜ From a model to an *agent* (tools, memory, planning, loops)

Legend: ✅ understood · ⏳ in progress · ⬜ not started

---

## Lesson Log

### Lesson 1 — The Dream & The Core Question  ✅

- **Core question (1950, Alan Turing):** "Can a machine think?"
- **Obstacle #1:** "Thinking" can't be defined → can't be built or tested.
- **Turing's decision:** Replace the vague question with a *testable* one —
  "Can a machine behave indistinguishably from a human?" (the **Turing Test**).
- **Why it matters:** AI became about **observable behavior and results**, not
  the philosophy of an inner mind. This mindset still drives today's AI.

### Lesson 2 — Symbolic AI (Rules & Logic)  ✅

- **Core belief:** "Intelligence = manipulating symbols according to rules."
- **Two ingredients:** (1) a **knowledge base** of human-written facts + if-then
  rules, (2) an **inference engine** that chains rules to reach conclusions.
- **Wins:** theorem provers, chess programs, 1980s **expert systems** (e.g.
  MYCIN diagnosing infections).
- **Defining trait (and future weakness):** *humans hand-write every rule in
  advance.* The machine is only as smart as its rules.

### Lesson 3 — The Obstacles That Broke Symbolic AI  ✅

Four walls, all rooted in "humans must hand-write every rule":
1. **Brittleness** — every rule needs endless exceptions (birds fly... except
   penguins, ostriches, injured ones...). Breaks outside what the author foresaw.
2. **Knowledge bottleneck** — humans writing rules by hand doesn't scale
   (e.g. **Cyc**, decades of manual rules, still not childlike common sense).
3. **Common-sense / frame problem** — near-infinite obvious-but-unstated facts
   ("water falls down") must all be spelled out explicitly.
4. **Perception** — can't write clean rules for "is this a cat?", speech, etc.
- **Consequence:** the **AI Winters** (1970s, late-80s/early-90s) — funding &
  hype collapsed.
- **THE PIVOT:** root cause = the human writing rules. Decision → *stop writing
  rules; show the machine examples and let it learn the patterns itself.* This is
  the birth of **Machine Learning**.

### Lesson 4 — Learning From Data (How "Learning" Actually Works)  ✅

- A "rule" is just a **function**: input → output. ML = let the machine *find*
  the function instead of a human writing it.
- **Trick:** pick a function with a fixed shape but **adjustable knobs =
  parameters / weights.** Learning = tuning the knobs.
- **The training loop:** guess → measure error (**loss**) → nudge knobs to
  shrink error → repeat. (Toy example: `score = w × hours`.)
- **Generalization** = the big win: it learns the *pattern*, so it answers
  inputs it never saw → escapes Symbolic AI's brittleness.
- Modern models = this *same loop*, just billions of knobs instead of one.

### Lesson 5 — The Perceptron (First Neuron) & The Flaw That Broke It  *(in progress)*

_Notes will be added here as we discuss._

