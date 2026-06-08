# From MERN to AI Engineer — A Learn-in-Public Roadmap

A competence-gated path from "full-stack dev who uses AI" to "AI engineer who can build anything and explain how it works under the hood." Built to produce a public trail (repos + posts) that a beginner could follow.

---

## How to read this

**Two tracks running in parallel, not in sequence.**

- **Builder spine** — you ship something real in every phase. You already think like a product engineer; we keep that muscle warm.
- **Fundamentals rail** — alongside each build, you learn the *why* underneath it, so you're never just gluing APIs together.

The mistake most MERN→AI transitions make is picking one: either three months of math before building anything (you quit), or building agents you can't debug because you don't know what a token is (you plateau). The two tracks fix both.

**Phases gate on competence, not weeks.** You advance when you can *build the deliverable and explain the concept to a beginner*, not when a calendar says so. Rough effort estimates are given, but treat them as loose.

**Everything produces a repo + a post.** Documentation isn't a chore bolted on at the end — it's the forcing function. If you can't write the explainer, you don't understand it yet. This is also how the public trail gets built.

---

## Your starting point (why this plan is shaped for you)

**Already strong — we will not re-teach these:**
- Production full-stack: Next.js, Node, TypeScript, MongoDB, Redis, WebSockets, payments, microservices.
- RAG in production: pgvector, embeddings, chunking (Mintmark).
- Agentic orchestration: Trigger.dev multi-agent pipeline, BYOK LLM adapter across providers.
- Daily agent harness use: Claude Code is already your primary dev tool.

**Real gaps — this is where the plan spends its energy:**
1. **Python fluency** for the AI/data stack (you've done Python for interviews, but not lived in numpy/pandas/PyTorch).
2. **ML/DL fundamentals** — what a model actually is, backprop, why transformers work.
3. **The "why" under the things you already use** — tokens, attention, context windows, sampling, what makes an agent reliable.

So you start at Phase 0 for setup and Phase 1 for fundamentals, but you move *fast* through anything that overlaps what you've already shipped. Your Claude Code intuition becomes a genuine superpower in Phases 3–4, where most people are starting cold.

---

## The documentation system (set up once in Phase 0, use forever)

**GitHub — a hub-and-spoke layout:**

```
ai-in-public/                  ← the hub repo (this file can be its README/ROADMAP)
├─ README.md                   ← the roadmap + a live progress log
├─ notes/                      ← one markdown file per concept, in your own words
│   ├─ transformers.md
│   ├─ rag-that-works.md
│   └─ agent-loop.md
├─ projects/                   ← short index + links to each project repo
└─ log.md                      ← dated, raw "what I learned today" entries

<project repos live separately, each with a beginner-readable README>
build-gpt-from-scratch/
rag-eval-harness/
agent-from-first-principles/
...
```

The hub repo is the front door a beginner lands on. Each project repo has a README written so someone with your *current* JS background (but no AI) could reproduce it.

**Blog — own the canonical copy, syndicate everywhere:**
- **Canonical home:** your Next.js portfolio site. You already built an MDX + RAG ingestion pipeline for it — write posts as MDX, they feed your own RAG, and you own the content forever.
- **Syndicate:** repurpose each post into an X thread and a LinkedIn post (you already have this LinkedIn→X workflow running). Concept explainers thread beautifully.
- **Cadence:** one "build log" per phase milestone + the occasional standalone "concept explainer" when something finally clicks. Don't force daily posts; force *honest* ones.

**The ethos:** swyx's two essays are the playbook — *Learn in Public* and *The Rise of the AI Engineer*. Read both before you write your first post.

---

## Phase 0 — Python, environment, and the public scaffold
*Effort: ~1 week. Goal: be dangerous in Python and have the trail set up.*

**Understand**
- Python the way the AI stack actually uses it: type hints, `dataclass`/Pydantic, async, comprehensions, then the data trio — `numpy`, `pandas`, `matplotlib`. Skim what's identical to JS; spend time only on what's different (slicing, broadcasting, the data model).

**Build**
- Set up `uv` (modern, fast Python package/proj manager), a Jupyter/Colab workflow, and a clean repo.
- Port one tiny thing you've written in JS to Python, just to feel the language.

**Resources**
- Official Python tutorial (fast for an existing programmer): https://docs.python.org/3/tutorial/
- `uv`: https://docs.astral.sh/uv/
- For the data trio, learn just-in-time — don't pre-study pandas; pick it up when Phase 1 needs it.

**Ship**
- Create the `ai-in-public` hub repo with this file as the README.
- Write **Post #0: "Why a MERN dev is learning AI from the fundamentals (and doing it in public)."** Set the narrative. This is your origin-story post — lean into it.

---

## Phase 1 — How LLMs actually work + your first from-scratch builds
*Effort: ~3–4 weeks. Goal: you can explain a transformer to a beginner and call a model API with zero framework.*

**Understand (this is the heart of "knows how modern AI works")**
- **Intuition first:** 3Blue1Brown's neural networks series, including the "what is a GPT / attention" videos. Pure visual intuition. https://www.3blue1brown.com/topics/neural-networks
- **The big-picture talks:** Andrej Karpathy's *Intro to LLMs* and *Deep Dive into LLMs like ChatGPT* (general-audience, under-the-hood). Linked from https://karpathy.ai/
- **Build it to understand it:** Karpathy's *Neural Networks: Zero to Hero* — micrograd → makemore → "Let's build GPT" → the tokenizer video. This is the canonical from-scratch course; it assumes only Python + vague calculus. https://karpathy.ai/zero-to-hero.html · code: https://github.com/karpathy/nn-zero-to-hero
- **The frame for everything after:** start Chip Huyen's *AI Engineering* (Ch. 1–3: the AI stack, foundation models, intro to evaluation). https://huyenchip.com/books/ · free resources: https://github.com/chiphuyen/aie-book

**Build (builder spine)**
- Talk to a model through the **raw API, no framework** (Anthropic and/or OpenAI). Feel tokens, context windows, temperature/sampling, structured output, and tool/function calling at the metal. You've used these via abstractions — now ground them.
- Anthropic prompt-engineering docs + cookbook: https://docs.claude.com · https://github.com/anthropics/anthropic-cookbook

**Ship**
- Repo: `build-gpt-from-scratch` (your worked-through Karpathy GPT, heavily commented for beginners).
- **Post: "I built GPT from scratch — here's what 'attention' actually does."** Written in your own words, with diagrams. This is the post that proves to you (and your audience) that you get it.

---

## Phase 2 — Retrieval & RAG done *properly* + your first eval harness
*Effort: ~2–3 weeks. Goal: RAG that you can prove works, not vibes.*

You've shipped pgvector RAG, so this phase is about leveling from "it works on my five test queries" to "I can measure and defend it."

**Understand**
- Chunking strategies, embedding quality, and **hybrid search**: why dense vectors handle "what are our design principles?" but you still need BM25/keyword for exact-match queries like a function name. (This exact-vs-semantic split is also a core harness-engineering insight you'll reuse in Phase 4.)
- Reranking, and how to *evaluate retrieval* rather than eyeball it.
- Chip Huyen *AI Engineering* — the RAG + agents chapter; Hugging Face's LLM course for hands-on. https://huggingface.co/learn

**Evals — start here, it's the single highest-leverage skill**
- Hamel Husain, *Your AI Product Needs Evals* — error analysis, code-based assertions, LLM-as-judge done so you can trust it. https://hamel.dev/blog/posts/evals/index.html
- The AI Evals course (Hamel Husain & Shreya Shankar) if you want the structured version.

**Build**
- Rebuild a small RAG app *and* an eval harness for it: a labeled question set, retrieval metrics, and an LLM-judge you've validated against your own labels.

**Ship**
- Repo: `rag-eval-harness`.
- **Post: "Why naive RAG fails, and how to actually measure retrieval."** (Pairs perfectly with your recent search-infra / Elasticsearch content — naive DB search vs purpose-built retrieval is the same story one layer down.)

---

## Phase 3 — Agents from first principles
*Effort: ~3–4 weeks. Goal: build a reliable agent loop you fully understand, then reach for frameworks deliberately.*

**Understand**
- Anthropic, *Building Effective Agents* — the canonical "don't reach for a framework first; understand the Thought→Action→Observation loop" piece. https://www.anthropic.com/engineering/building-effective-agents
- Tool use, **MCP (Model Context Protocol)** — learn this deeply; it's the standard your Claude Code already speaks. Memory (short-term context vs long-term retrieval). Multi-agent patterns and their token cost.

**Build**
- Write a minimal agent loop **by hand** (model + tools + loop + memory), no framework. Then re-implement it with a framework (e.g. LangGraph) so you understand exactly what the framework is buying you.
- Strong candidate: evolve **Peerly** into a properly agentic version — it's already an outreach/research agent at heart.

**Ship**
- Repo: `agent-from-first-principles`.
- **Post: "What an AI agent actually is (I built one without a framework first)."**

---

## Phase 4 — Context engineering & harness engineering (the frontier)
*Effort: ~3–4 weeks. Goal: take an agent from "demo" to "reliable for hours unsupervised." This is where you pull ahead.*

Your daily Claude Code use means you already have *felt* intuitions here that most learners lack. Now you make them explicit.

**Understand**
- **Context engineering** — Anthropic, *Effective context engineering for AI agents*: context is a finite resource; the job is curating the smallest set of high-signal tokens. Compaction, just-in-time retrieval, tool-set discipline. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- **Harness engineering** — the discipline of everything-around-the-model: **Agent = Model + Harness**. The harness is your guides (system prompts, AGENTS.md/CLAUDE.md, constraints) and your sensors (evals, validation loops, parsers). Failures are engineering problems to fix permanently, not prompts to retry.
  - The curated entry point: https://github.com/ai-boost/awesome-harness-engineering (links Mitchell Hashimoto's originating posts)
  - OpenAI's framing: https://openai.com/index/harness-engineering/
  - Martin Fowler's piece (harness engineering for coding-agent users): https://martinfowler.com/articles/harness-engineering.html

**Build**
- Take your Phase 3 agent and engineer a real harness around it: a proper system prompt + constraint doc, sub-agents as context firewalls, deterministic validation hooks, and the eval harness from Phase 2 acting as sensors. Measure reliability before vs after.

**Ship**
- **Post: "Agent = Model + Harness — what I learned making mine reliable."** This is the post that signals you're operating at the current frontier, not last year's tutorial level.

---

## Phase 5 — Production, fine-tuning, specialization + capstone
*Effort: open-ended. Goal: a flagship AI-native product + the depth to go anywhere.*

**Understand**
- When fine-tuning is worth it vs. prompting/RAG (mostly: it usually isn't — know *why*). Chip Huyen's later chapters.
- Serving, latency/cost optimization, inference economics, observability, and the security/privacy layer (you already know AES-256-GCM, rate limiting — connect it to AI-specific risks like prompt injection and excessive agency).
- Optional deep dive: finish *Zero to Hero* and study Karpathy's nanoGPT / nanochat for end-to-end understanding.

**Build — the capstone**
- A flagship, AI-native product that exercises the whole stack: RAG + agents + a real harness + evals + production concerns. Strong options: a deeply AI-native **Mintmark v2**, or **Peerly** taken to production. You like a defensible flagship — make this one.

**Career layer**
- swyx, *The Rise of the AI Engineer* — the role you're growing into, and how to position. https://www.latent.space/p/ai-engineer
- Latent Space podcast for staying current; the AI Engineer community/conf for the ecosystem.

---

## The canonical resource shelf (bookmark these)

**Foundations & how models work**
- Karpathy — *Neural Networks: Zero to Hero* + LLM talks · https://karpathy.ai/
- 3Blue1Brown — neural networks / transformers (visual intuition)
- fast.ai — *Practical Deep Learning for Coders* (top-down, builder-friendly) · https://course.fast.ai/

**The AI engineer's core**
- Chip Huyen — *AI Engineering* (the book for your goal) · https://huyenchip.com/books/ · https://github.com/chiphuyen/aie-book
- Hugging Face — LLM course + Agents course · https://huggingface.co/learn
- DeepLearning.AI — short courses on agents, RAG, evals · https://www.deeplearning.ai/

**Agents, context, harness (the frontier)**
- Anthropic Engineering — *Building Effective Agents* + *Effective Context Engineering* · https://www.anthropic.com/engineering
- awesome-harness-engineering · https://github.com/ai-boost/awesome-harness-engineering
- Anthropic cookbook + docs · https://github.com/anthropics/anthropic-cookbook · https://docs.claude.com

**Evals (do not skip)**
- Hamel Husain — *Your AI Product Needs Evals* · https://hamel.dev/blog/posts/evals/index.html

**Career & learning-in-public**
- swyx — *The Rise of the AI Engineer* + *Learn in Public* · https://www.latent.space/ · https://www.swyx.io/learn-in-public

---

## A note on pace and honesty

Don't speedrun Phase 1 to get to the cool agent stuff — the fundamentals are exactly what will let you debug agents when they break in production, which is the thing that separates AI engineers from prompt-tinkerers. But also don't get stuck doing math forever: you're a builder, and shipping is how you'll actually consolidate this. When in doubt, build the deliverable and write the post. The post is the test.
