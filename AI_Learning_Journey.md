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
5. ✅ The first neural network (the perceptron) — and what broke it
6. ✅ Backpropagation — teaching networks to learn
7. ✅ Deep learning — depth, data, and GPUs
8. ✅ Representing meaning (word embeddings)
9. ⏳ Handling sequences (RNNs / LSTMs) and their limits  ← **RESUME HERE NEXT**
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

### Lesson 5 — The Perceptron (First Neuron) & The Flaw That Broke It  ✅

- **Inspiration:** the brain's neuron — receives signals, "fires" if the
  combined signal clears a threshold. Rosenblatt (1957) built one: the
  **perceptron.**
- **Mechanism:** weigh each input (weights = the knobs), sum them, fire (1) if
  sum > threshold else 0. Learns weights via the same guess→check→adjust loop.
- **Huge hype** in 1958, then **the wall (Minsky & Papert, 1969):** a single
  perceptron can only separate data with **one straight line** (linearly
  separable) → **can't even solve XOR** (fire if inputs differ).
- **Consequence:** the connectionist/neural-net winter (~a decade).
- **Visible-but-blocked fix:** stack neurons in **layers** (a neural network) —
  but nobody knew **how to train the hidden middle layers** (no "right answer"
  for them). → solved next by **backpropagation**.

### Lesson 6 — Backpropagation (Teaching the Hidden Layers)  ✅

- **The blocking problem:** stacked neurons *can* solve XOR, but the hidden
  middle layers have **no target answer** to compare against — so how do you
  tune their knobs? This is the **credit/blame assignment problem.**
- **Key reframe:** a network is just **functions inside functions**
  (`output = layer3(layer2(layer1(input)))`). The loss at the end depends on
  every weight, deep ones included, through a **chain** of steps.
- **What we need per weight:** the **gradient** — the slope of error vs. that
  weight (which way + how steeply to nudge it). Nudging downhill = **gradient
  descent** (same idea as Lesson 4, now for buried knobs).
- **The chain rule:** a nudge travels through a chain of steps; **multiply each
  link's local rate** to get the deep weight's effect on the loss (rates
  compound → multiply, not add). Each neuron only needs its own local rate.
- **Backpropagation = two passes:** (1) **forward** — run input through, compute
  the loss; (2) **backward** — push the error backward layer by layer, each layer
  computing its own weights' gradients *and* how much the previous layer's output
  must change, passing that back. Shared chunks get reused → fast.
- **Then:** gradient descent nudges every weight; repeat forward→backward→nudge
  millions of times. Same **guess→check→adjust** loop, now working through any
  depth.
- **Why it mattered:** **Rumelhart, Hinton & Williams (1986)** popularized it,
  answering Lesson 5's blocking question. Networks could finally go **deep** and
  learn internal features nobody hand-designed. Still how every modern net
  (GPT included) learns.

### Lesson 7 — Deep Learning: Depth, Data, and GPUs  ✅

- **The puzzle:** backprop made deep nets trainable in 1986, yet the revolution
  waited until **~2012**. Three things had to arrive *together*.
- **What depth buys:** layers build a **hierarchy of features** (pixels → edges →
  parts → objects). The net **invents its own features** (representation
  learning) — finally cracking Symbolic AI's **Obstacle #4 (perception)** without
  hand-written rules.
- **Why it stalled 25 years — three walls:**
  1. **Too little data** → millions of knobs **overfit** (memorize, don't
     generalize).
  2. **Too little compute** → training took months on CPUs.
  3. **Vanishing gradients** → the chain rule (Lesson 6) multiplies small local
     rates (old `sigmoid`) → gradient ≈ 0 at early layers → they won't learn.
- **What broke the walls (~2012):** **ImageNet** (~14M labeled images = data);
  **GPUs** (built for parallel **matrix multiply** = exactly neural-net math →
  10–100× faster); **ReLU** + better init (rate stays 1 → gradients survive).
- **Watershed:** **AlexNet (2012)** demolished the ImageNet contest → modern AI
  era begins.
- **The formula:** **depth + big data + GPUs**, all at once. Remove any one and
  it collapses — which is why 1986's trainable nets had to wait until 2012.

### Lesson 8 — Representing Meaning (Word Embeddings)  ✅

- **The entry problem:** networks only do math on numbers — so how do you feed a
  *word* ("king") to one?
- **Naive fails:** (1) **word IDs** (`king=1, queen=2`) smuggle in false
  arithmetic/ordering; (2) **one-hot** vectors (one `1` in a 50k-long vector) are
  huge, sparse, and make *every* word equidistant → encode identity but **zero
  similarity**.
- **The idea — word embeddings:** each word = a short **dense** vector (~300
  numbers) positioned so **meaning = geometry**. Similar words sit **close**
  (`cat`↔`dog` near, `cat`↔`democracy` far).
- **Learned, not assigned:** trained from data via the **distributional
  hypothesis** — *"know a word by the company it keeps."* Train a net to predict a
  word from its neighbors (**word2vec, 2013**); meaningful vectors fall out as a
  **side effect**.
- **The magic:** relationships become **consistent directions** →
  `king − man + woman ≈ queen`, `Paris − France + Italy ≈ Rome`. Word arithmetic
  works because meaning is encoded as geometry.
- **Why it matters:** this is **layer zero** of every LLM — GPT first embeds each
  token into a meaning-vector. Everything later (sequences, attention) runs on
  these vectors.

