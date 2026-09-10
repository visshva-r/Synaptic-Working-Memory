# Blog: Making interference visible — synaptic working memory for DataForge

## The sentence we are teaching

A fixed-shape synaptic state can absorb a stream of any length without a new memory slot per token — until a similar cue retrieves the wrong fact.

That sentence is falsifiable. If raising key similarity never hurts the synaptic probe, the demo is wrong. If lowering similarity never recovers the truth, the demo is also wrong. The lab is built so either failure is visible in under a minute.

## Why this topic (and not a survey)

The Pathway brief rewards one claim, a behaving substrate, and a real BDH module. “Explain all of post-Transformer AI” fails that test. Synaptic plasticity as short-term memory is on the approved list and is native to BDH’s story: attention as synaptic memory, Hebbian writes during inference, associations in wiring rather than only in a growing cache.

## What you do in the artifact

The page opens already writing a preset stream: A→RED, then C→GREEN, B→BLUE, C→GREEN, B→BLUE, C→GREEN.

- **Left:** a Transformer-style KV picture. Each fact gets a slot. Length grows.
- **Right:** an 8×8 matrix \(W\) with \(W \leftarrow (1-\gamma)W + \eta(k\otimes v)\). Shape stays fixed.
- **Probe:** truth sits beside each estimate. Move **key similarity**. Watch the answer change.

At the default similarity of 0.72 the synaptic side answers **BLUE** to cue A, whose true value is RED, while the KV panel still answers RED. Drag similarity below about 0.39 and the synaptic answer flips back. That flip is the lesson.

The first build of this page did not earn that sentence. It wrote A→RED twice, including last, so the self-match always outvoted the interfering write: confidence dropped from 1.00 to 0.81, but the label stayed RED. Lower confidence is not a wrong association. The stream was rebuilt so A is written once and early while the overlapping key repeats later, which is what makes the claim testable instead of merely suggestive.

## BDH, without mythology

We cite Kosowski et al. (arXiv:2509.26507) for the architectural claim that working memory can live in synaptic plasticity. We cite BDH-CQ (arXiv:2608.09888) to keep a clean distinction: CQ is not “the same slider with a new logo.” We label our matrix a **toy**. We refuse to call BDH a Mamba SSM. We refuse to present Pathway blog figures as live model behavior.

## What we are not claiming

- We did not reproduce Sudoku Extreme or ARC numbers.
- We did not run official BDH weights.
- Soft attention can interfere too; the KV panel uses sharp nearest-key retrieval to isolate the *allocation* contrast.

## How to critique us in one minute

1. Replay with similarity ≈ 0.72, probe A — synaptic should answer BLUE while KV answers RED.
2. Similarity ≈ 0.1 — synaptic should recover RED.
3. Ask us on finals day where the crossover sits. The answer is `s* = u⁴/(u² + 1)` with `u = 1 − γ`, and η does not appear in it — η scales both traces equally, so the sliders are not interchangeable. If we could not derive that, we would not own the code.

## Submission note

This blog accompanies the interactive `index.html` and the one-page concept summary. Together they are the Pathway package: claim, substrate, BDH module, limitations, sources.
