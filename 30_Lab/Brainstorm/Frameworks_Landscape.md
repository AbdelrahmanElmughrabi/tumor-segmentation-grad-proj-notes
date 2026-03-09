---
type: brainstorm
---

# Frameworks Landscape

Parent: [[Brainstorm]]

## From Open Source Research

### MONAI
PyTorch-based medical imaging library. Not a project — a tool you install and use.
Handles: NIfTI loading, medical transforms, U-Net blocks, Dice loss, CacheDataset for fast I/O.
Auto3DSeg: automatically selects and ensembles models for 3D segmentation tasks.
Tutorials include BraTS and TCIA dataset examples.
Best for: building our pipeline backbone.
Link: https://github.com/Project-MONAI/tutorials

### nnU-Net
Self-configuring segmentation framework. Extracts dataset fingerprint and auto-configures preprocessing, normalization, architecture, patch size.
Strength: nearly guaranteed strong baseline, zero manual config.
Weakness: not easily adapted for multi-task learning (adding classification head).
Best for: generating a strong segmentation baseline to compare against.

### Key Insight
The field has shifted from architectural engineering to data engineering. nnU-Net automates architecture search — the researcher's role is now clean data and correct evaluation. For our project: spend more effort on preprocessing quality than architecture tweaking.

### SAM2 (Zero-shot reference)
Adapts Meta's video tracking to medical imaging — propagates a mask from one annotated slice through the entire volume.
Input: one bounding box → center-outward propagation.
Training-free. Useful for rapid sanity checks or baselines without any training.
Not suitable as primary approach (no classification, no Grad-CAM).

## Sources
→ [[Open_Sourced_Sources]]
