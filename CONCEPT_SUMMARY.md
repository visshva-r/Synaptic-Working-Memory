# Synaptic plasticity as short-term memory — one-page concept summary

**DataForge 2026 · Pathway track · Team Think Loop (solo)**  
**Central claim:** A fixed-shape synaptic state can process a stream of unbounded length without allocating a new memory slot per token, but similar cues interfere and can retrieve the wrong association.

## Design pressure

Transformers retain context with a growing key–value cache. That design is accurate and observable, yet memory and compute scale with sequence length. A recurring alternative is a **fixed-size associative state**: write into connections (or fast weights), read by cue, accept interference as the capacity cost. This is not a generic “memory in AI” primer. It is one mechanism — **synaptic / Hebbian short-term memory** — chosen because Dragon Hatchling (BDH) makes it architectural rather than bolted on.

## Mechanism

A teaching form of the write is:

\[
W \leftarrow (1-\gamma)W + \eta\,(k \otimes v)
\]

A probe \(q\) reads \(\hat{v} = Wq\). When two keys are nearly colinear, their outer products overlap and retrieval mixes values. Similarity alone is not sufficient for a *wrong* answer: a cue matches its own key at 1.0 and an overlapping key at only \(s<1\), so one competing write lowers confidence without changing the label. Interference wins the label when overlapping writes accumulate while the original trace decays. In the artifact's preset, `A→RED` is written once and early and the overlapping key is written twice and later; the synaptic read for cue A crosses from RED to BLUE at similarity \(s^\* = u^4/(u^2+1)\), \(u = 1-\gamma\) — 0.39 at the default decay — while the KV cache, holding a dedicated slot, stays correct throughout. Write strength \(\eta\) cancels from that expression, which is a small but useful reminder that not every knob is a control variable. The artifact places **truth beside estimate** with mixture shares, so the learner can falsify the claim by lowering similarity until the probe recovers.

This simulation is an **independent toy**. It is not an official BDH checkpoint and must not be described as one. It also is **not** a Mamba-style state-space model; the Pathway brief explicitly separates BDH-GPU / ReLU-low-rank formulations from SSM classification.

## BDH and BDH-CQ

**BDH** (Kosowski et al., arXiv:2509.26507) presents a brain-inspired post-Transformer family in which reasoning and memory share one fabric, with attention related to synaptic memory updated during reading. Public materials emphasize sparse non-negative activations, monosemantic synapses at concept scale, and a GPU-friendly formulation. Working memory during inference is described via synaptic plasticity / Hebbian dynamics rather than only an ever-growing explicit token store. Evidence level: **developer-reported architecture and evaluations in the paper**; the open toy repo is educational and does not by itself reproduce every headline benchmark.

**BDH-CQ** (arXiv:2608.09888) sits in the same family with a different operational story: skill from demonstrations, latent reasoning without a written chain of thought, and adaptation framed through recurrent state rather than evaluation-task fine-tuning. Relevance here is comparative, not identical: both reject “memory = only the KV list,” but CQ should not be flattened into Hebbian outer products. If a sentence only needs BDH, say so.

## Landscape (compact)

| Approach | What stays bounded | Main trade-off |
|----------|--------------------|----------------|
| Transformer KV cache | Model weights; cache grows | Memory/latency with length |
| Linear attention / fast weights | Often fixed state size | Expressivity & interference |
| Selective SSMs (e.g. Mamba) | Recurrent state | Different inductive bias than BDH |
| BDH synaptic memory | Associative state in wiring | Interference; evidence still maturing outside developer reports |

## Advantage, weakness, maturity

**Advantage (conceptual):** constant-shape state can follow long streams without a new slot per token, and makes “where the memory lives” inspectable as a matrix of associations.  
**Weakness:** interference under similar cues; low-dimensional toys exaggerate it; sparsity, inhibition, and scale-free connectivity in BDH are absent from the demo.  
**Maturity:** post-Transformer memory research is active (2022–2026 linear attention, SSM, xLSTM, BDH). Treat BDH reported scaling and puzzle results as **author-reported** unless independently reproduced. Partnerships or blog equations are not substitutes for external replication.

## Limitation to keep

The most important unanswered piece for a learner is consolidation: when should useful fast synaptic state become durable slow weights? The artifact does not solve that; it only makes interference measurable.

## Where to continue

Primary: arXiv:2509.26507, arXiv:2608.09888, Pathway “From Attention to Synapses,” “Equations of Reasoning,” github.com/pathwaycom/bdh. Contrast: LoRA (parametric adaptation), Mamba (SSM), xLSTM (recurrent memory revival). Artifact: open `index.html`, run the sixty-second test in the README.
