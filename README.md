# Synaptic Working Memory

**Team:** Think Loop (solo)  
**Event:** DataForge 2026 · Pathway track  
**Topic:** Synaptic plasticity as short-term memory  

| | |
|--|--|
| **Live artifact (no sign-in)** | https://visshva-r.github.io/Synaptic-Working-Memory/ |
| **Source repository** | https://github.com/visshva-r/Synaptic-Working-Memory |
| **Open locally** | [`index.html`](./index.html) |

## One-sentence claim

A fixed-shape synaptic state can absorb a stream of any length without allocating a new memory slot for every token, but a later similar cue can retrieve the wrong association when two writes interfere.

## Audience and prerequisites

- **Audience:** data scientists / ML engineers who know Transformers and KV caching at a high level.
- **Prerequisites:** vectors, outer products, basic attention intuition.
- **Not required:** running BDH training or access to proprietary checkpoints.

## Learning objectives

After ~60 seconds with the lab, a learner should be able to:

1. State the claim in their own words.
2. Change **key similarity** and predict whether the synaptic probe will match ground truth, including where it flips to the wrong answer.
3. Contrast growing KV allocation with fixed Hebbian state.
4. Place the idea in **BDH** (synaptic working memory) and distinguish **BDH-CQ** (recurrent-state adaptation without verbal CoT / without eval-time weight updates as framed in the PS).
5. Name at least one limitation (interference needs repetition or decay, not similarity alone; ignored sparsity; toy ≠ official model).

## How to run

```bash
# Option A — open the public Pages URL above (preferred for judges)

# Option B — double-click / open in browser
open index.html

# Option C — local static server
python -m http.server 8080
# then visit http://localhost:8080
```

No sign-in. No API keys. Works offline after fonts load (or with system fallbacks).

## What is live vs toy vs illustration

| Part | Status |
|------|--------|
| Dual-panel lab (KV slots vs `W` matrix) | **Live computation** in the browser |
| Hebbian update `W ← (1−γ)W + η (k ⊗ v)` | **Teaching toy**, independent reimplementation |
| Color decode / confidence | Heuristic visualization, not a trained head |
| BDH / BDH-CQ narrative | From **primary papers and Pathway writeups**, not a run of official weights |
| Animations | None presented as model inference |

**Do not treat this page as an official BDH or BDH-CQ model.** The Pathway problem statement allows toy models when labeled.

**Do not classify BDH as a Mamba-style SSM.** The PS forbids that; Mamba is cited only as a contrast.

## Architecture of the artifact

1. **Preset stream** writes `A→RED`, `C→GREEN`, `B→BLUE`, `C→GREEN`, `B→BLUE`, `C→GREEN` on a timer (page opens already running). `A` is written once and early; the overlapping key `B` is written twice and later.
2. **KV panel** stores one slot per write (memory grows).
3. **Synaptic panel** keeps an 8×8 matrix and applies decay + Hebbian write.
4. **Probe** retrieves nearest-key value (KV) vs `W q` (synaptic) and shows **truth beside estimate**, plus the mixture shares.
5. **Controls map to concept variables only:** similarity, η, γ, probe cue.

### Why the stream is ordered that way

A cue matches its own key at 1.0 and an overlapping key at only `s < 1`, so a *single* competing write can never outvote the original — it only lowers confidence. To make the claim's "wrong association" literally true, the overlapping key is written twice while `A`'s trace decays. With default η = 0.55, γ = 0.08, the synaptic read for cue `A` crosses from RED to BLUE at **similarity ≈ 0.39**:

| similarity | RED mass | BLUE mass | synaptic answer |
|---|---|---|---|
| 0.10 | 0.362 | 0.093 | RED (correct) |
| 0.30 | 0.362 | 0.280 | RED (correct) |
| 0.40 | 0.362 | 0.374 | **BLUE (wrong)** |
| 0.72 | 0.362 | 0.673 | **BLUE (wrong)** |

KV answers RED at every setting, because it kept `A` a dedicated slot.

The crossover has a closed form for this stream. Probing `A`, the RED mass is `η u⁵` and the BLUE mass is `η s (u³ + u)` with `u = 1 − γ`, so the two are equal at:

```
s* = u⁴ / (u² + 1)        u = 1 − γ
```

γ = 0 → 0.500, γ = 0.08 → 0.388, γ = 0.25 → 0.203, γ = 0.40 → 0.095. **η cancels**: it scales both traces equally and cannot move the crossover. `python _verify.py` checks the closed form against the simulation by bisection (they agree to 4 decimal places).

## BDH module

BDH’s public paper describes working memory during inference via synaptic plasticity / Hebbian updates — associations live in connections over a short horizon rather than only as an ever-growing explicit token store. This explainer’s claim is that **fixed-shape associative state buys unbounded stream length at the cost of interference**.

BDH-CQ is related but not identical: treat it as the same research family with a different emphasis on demonstration-driven / latent reasoning without requiring a written chain of thought, and without collapsing it into “Hebbian writes only.” See the concept summary PDF for evidence labels.

## Primary sources

- Kosowski et al., *The Dragon Hatchling*, https://arxiv.org/abs/2509.26507
- BDH-CQ technical report, https://arxiv.org/abs/2608.09888
- Pathway: [From Attention to Synapses](https://pathway.com/research/bdh-explainer/bdh-architecture-derivation)
- Pathway: [Why BDH Uses a Brain-Inspired Architecture](https://pathway.com/research/bdh-explainer/brain-inspired-ai-architecture)
- Pathway: [The Equations of Reasoning](https://pathway.com/research/the-equations-of-reasoning)
- Official toy code: https://github.com/pathwaycom/bdh
- Contrast papers: LoRA (2022), Mamba (2023), xLSTM (2024) — linked in `index.html`

## Package checklist

- [x] Public artifact URL (GitHub Pages)
- [x] Public source repository
- [x] Blog PDF
- [x] One-page concept summary PDF
- [x] README (this file)
- [x] AI / license disclosure (below)
- [x] ≥3 recent primary papers cited beside claims

## AI assistance disclosure

- **Cursor Agent / Auto / Composer-class models** assisted with HTML/CSS/JS scaffolding, README, and summary drafts.
- **Human ownership:** claim selection, topic lock (synaptic plasticity), judging-criteria mapping, source list, and final wording/defense responsibility sit with the registered solo participant.
- No official BDH weights were copied. No Rime track code is included.
- Forks: none. This repo is original teaching code inspired by published equations and explainer design norms (Transformer Explainer–style pedagogy, not a fork).

## License

Code in this repository: MIT (see below). Papers and Pathway blog content remain under their respective licenses; cite, do not republish wholesale.

```
MIT License. Copyright (c) 2026 Think Loop / Visshva R

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED.
```
