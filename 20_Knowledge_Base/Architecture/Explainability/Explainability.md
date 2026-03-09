---
type: knowledge
---

# Explainability

Parent: [[Architecture]]

## From Open Source Research

### Why XAI in Medical Imaging
Clinicians cannot act on a black-box prediction in a clinical context where decisions affect lives. Explainability bridges the trust gap. Also satisfies the complex system requirement by adding an interpretability layer.

### Grad-CAM
Post-hoc visualization — no architectural changes, no retraining required.

**Mechanism:**
1. Forward pass through trained model
2. Compute gradient of target class score with respect to final conv layer feature maps
3. Global average pool gradients → importance weight per feature map channel
4. Multiply feature maps by weights, sum, apply ReLU
5. Upsample to input resolution, overlay as heatmap

ReLU is critical — suppresses negative activations, shows only what positively influenced the prediction.

**Compute cost:** ~20-35ms per image. Negligible overhead.

### Seg-Grad-CAM
Adaptation for segmentation output (dense prediction, not scalar).
Aggregation: sum all predicted probabilities for a target class across the spatial mask extent → use this sum as the scalar gradient target.
Result: heatmap showing which input regions most influenced segmentation of a specific tumor region.

### Interpreting Heatmaps
- ✅ Good: high activations tightly aligned with tumor boundaries on relevant modality
- ❌ Bad: high activations on background, healthy tissue, or image borders — model is relying on artifacts regardless of Dice score

### Reference for Mammography
**BreastCancerDiagnosisMRI** applies Grad-CAM to DCE-MRI — outputs probability per slice + Grad-CAM on maximum probability slice. Pattern transferable to mammography.

### Implementation Library
`jacobgil/pytorch-grad-cam` — hooks directly into PyTorch U-Net layers. Supports both classification and segmentation Grad-CAM.

## From Literature / Papers
*(To be added during literature review phase)*

## Sources
→ [[Open_Sourced_Sources]]
