---
type: knowledge
---

# Normalization Strategy

Parent: [[Segmentation]]

## From Open Source Research

### The Batch Normalization Problem at Small Batch Sizes
Batch Normalization calculates mean and variance across the batch dimension. At batch size 1 or 2 (required for 3D on 16GB VRAM) statistics become unstable and no longer represent the global distribution. Training fails to converge properly.

### Instance Normalization
Calculates statistics per channel per individual sample. Completely independent of batch size.
**Rule: for any 3D model training at batch size 1 or 2, replace Batch Normalization with Instance Normalization.**
nnU-Net enforces this automatically. Custom 3D U-Nets must implement this manually.

### Group Normalization
Divides channels into groups, calculates stats per group per sample. Also batch-size independent. Less common than Instance Norm in literature but valid alternative.

### 2D Models
At larger batch sizes (16, 32, 64) Batch Normalization works fine. This issue is specific to 3D training under memory constraints. 2D mammography pipeline can use standard Batch Normalization.

## From Literature / Papers
*(To be added during literature review phase)*

## Sources
→ [[Open_Sourced_Sources]]
