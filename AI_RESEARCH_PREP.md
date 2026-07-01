# AI Research Engineer — Prep Tracker

**Goal:** AI Research Engineer fellowship/internship · **Budget:** 4 hrs/day (~28 hrs/wk) · **Target:** apply by Week 9–10

**Spine project:** Build a small GPT from scratch → train → benchmark. Public repo, **commit daily**. Phase 4 extends it into a paper reproduction (your portfolio centerpiece).

**Rules (every phase):**
- [ ] Code daily, commit daily — git history = evidence
- [ ] Implement before watching the solution — struggle first
- [ ] Read 1 paper/week from Week 3 on (even if 50% lands)
- [ ] Don't gold-plate math — hit the gate, move on, return as needed

---

## Phase 1 — Math Refresh (Weeks 1–3)
> Goal: read ML math without stalling. Fluency, not mastery.

### Week 1 — Linear Algebra
- [ ] 3Blue1Brown *Essence of Linear Algebra* (full series)
- [ ] Focus: vectors, matmul as transformation, dot product, matrix-vector, rank, eigenvectors
- [ ] Redo each by hand on paper (no passive watching)
- [ ] **Deliverable:** NumPy notebook — matmul, dot product, 2D linear transform from scratch

### Week 2 — Calculus + Gradients
- [ ] 3Blue1Brown *Essence of Calculus* (skim)
- [ ] Focus: derivatives, chain rule, partial derivatives, gradient = steepest ascent
- [ ] **Deliverable:** hand-derive gradient of a 2-layer function, verify with finite differences in NumPy

### Week 3 — Probability + Optimization
- [ ] Topics: distributions, expectation, variance, softmax, cross-entropy, log-likelihood
- [ ] Gradient descent: learning rate, convexity, local minima
- [ ] **Deliverable:** GD from scratch to fit a line + logistic regression; plot loss curve
- [ ] **GATE:** read softmax + cross-entropy eqn → implement in NumPy unaided

---

## Phase 2 — ML Core Re-Up (Weeks 4–6)
> Goal: rebuild foundation, hand-implement backprop.

### Week 4 — Karpathy Zero to Hero (micrograd)
- [ ] Build `micrograd` — tiny autograd engine from scratch ⭐ **most important week**
- [ ] Implement backprop by hand
- [ ] **Deliverable:** working micrograd, tested against PyTorch autograd on a small example

### Week 5 — Neural Net Fundamentals
- [ ] Karpathy makemore (bigram → MLP)
- [ ] Topics: layers, activations, weight init, over/underfitting, train/val split
- [ ] **Deliverable:** char-level MLP language model that generates text; track train vs val loss

### Week 6 — Training Dynamics
- [ ] Karpathy makemore advanced (activations, gradients, BatchNorm)
- [ ] Topics: batch/layer norm, LR schedules, vanishing/exploding gradients, regularization
- [ ] **Deliverable:** diagnose a training run — plot activation/gradient stats, fix a broken init, write up findings
- [ ] **GATE:** implement + explain backprop through a 2-layer net; debug a bad training run

---

## Phase 3 — Deep Learning + PyTorch + Transformers (Weeks 7–10)
> Goal: PyTorch fluency + working transformer = core project artifact.

### Week 7 — PyTorch Fluency
- [ ] Port Phase 2 MLP to PyTorch
- [ ] Learn: tensors, autograd, `nn.Module`, optimizers, dataloaders, `.to(device)`/GPU
- [ ] **Deliverable:** same model in clean PyTorch; loss matches scratch version

### Week 8 — Attention + Transformers (theory + build)
- [ ] Read *Attention Is All You Need*
- [ ] Karpathy "Let's build GPT" (nanoGPT lecture)
- [ ] **Deliverable:** self-attention head from scratch, by hand, every line commented

### Week 9 — Full GPT Build
- [ ] Build multi-head attention → transformer block → full small GPT
- [ ] Train on real data (TinyShakespeare → bigger corpus)
- [ ] **Deliverable:** working GPT generating coherent text; training script, config, logged metrics
- [ ] **Start applications in parallel** (apps open 6–9 months early — don't wait)

### Week 10 — Scale + Polish + Benchmark
- [ ] Experiment: vary model size, context length, LR; log results in a table
- [ ] Clean repo: README, one-command reproducible training, results plots, findings writeup
- [ ] **Deliverable:** production-clean GPT repo — portfolio centerpiece + base for Phase 4
- [ ] **GATE:** someone runs one command → trains a transformer; you can explain every component

---

## Phase 4 — Reproduction + Apply (after Week 10)
- [ ] Pick a paper extending your GPT (efficiency/attention variant, or scaling-law mini-study)
- [ ] Implement on your GPT, benchmark vs baseline
- [ ] Write SOP — name papers you admire, why, what you'd do next (specific, not generic)
- [ ] Line up recommendation letters from people who saw you do research
- [ ] Interview drills: implement attention / training loop from scratch on demand
- [ ] Target labs/programs: Anthropic Fellows, OpenAI Residency, EleutherAI, Cohere For AI (open collectives = best no-PhD on-ramp)

---

## Resources
- **Math:** 3Blue1Brown — Essence of Linear Algebra + Essence of Calculus
- **ML/DL:** Karpathy "Neural Networks: Zero to Hero"
- **Transformers:** *Attention Is All You Need* + Karpathy nanoGPT
- **Reproduction base:** nanoGPT-class small transformer

## Progress Log
<!-- date — what done — blockers -->
- 2026-06-16 — plan created — —
