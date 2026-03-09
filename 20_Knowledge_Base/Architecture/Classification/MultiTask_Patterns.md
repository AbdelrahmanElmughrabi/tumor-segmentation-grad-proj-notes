---
type: knowledge
---

# Multi-Task Patterns

Parent: [[Classification]]

## From Open Source Research

### Core Pattern: Shared Encoder + Dual Branches
Single encoder processes input → splits at bottleneck into:
1. **Segmentation decoder** — skip connections + upsampling → pixel-wise mask
2. **Classification head** — GAP → Dense layers → class prediction

Why this works: segmentation spatial constraints regularize the classification branch. Classification global semantics provide context to the segmentation branch. Both tasks improve each other.

### Classification Head Design
Applied to bottleneck features (most compressed, most semantic layer):

Bottleneck → Global Average Pooling → Dense(128) → Dropout(0.5) → Dense(64) → Dropout(0.5) → Sigmoid (binary) or Softmax (multi-class)

Global Average Pooling: averages each feature map channel spatially. Drastically fewer parameters vs standard flattening. Reduces overfitting.

### Benign/Malignant Mapping in Breast Datasets
- **BUSI (ultrasound):** explicit benign/malignant/normal labels — cleanest mapping
- **Mammography (BI-RADS):** radiologist scoring system, does not directly map to benign/malignant — needs research on how to convert for our classification branch. See [[Mammography_Gaps]] GAP-04.

### Loss Weighting
L_total = λ_seg × L_seg + λ_cls × L_cls

Reference from caumente/multi_task_breast_cancer: L_total = λ × L_dice + (1-λ) × L_focal

See → [[Loss_Functions]] for full explanation.

### Reference Implementations
- **caumente/multi_task_breast_cancer** — ultrasound, U-Net++, shared backbone, seg+class. Closest open source match to our pipeline concept on breast imaging.
- **Bi-CBMSegNet** — mammography, dual-module encoder-decoder, 97.81% Dice. Segmentation only, no classification branch — but strongest mammography segmentation reference found.

### Known Gap
No open source project found combining seg + class + Grad-CAM for breast mammography specifically. See [[Mammography_Gaps]] GAP-01.

## From Literature / Papers
*(To be added during literature review phase)*

## Sources
→ [[Open_Sourced_Sources]]
