---
type: knowledge
---

# Loss Functions

Parent: [[Segmentation]]

## From Open Source Research

### Dice Loss
Core loss for medical segmentation. Directly optimizes spatial overlap between prediction and ground truth.

Formula: Dice = 2|P∩G| / (|P| + |G|)

Why use it: handles severe class imbalance (background pixels vastly outnumber tumor pixels) by measuring overlap ratio rather than pixel count.

### Cross-Entropy Loss
Standard pixel-wise classification loss. Problem in medical imaging: background class dominates — model learns to predict background everywhere and still achieves low loss. Never use alone for segmentation.

### Dice + Cross-Entropy (Combined)
Most common combination in medical segmentation. Dice handles global overlap accuracy, CE handles pixel-level certainty. Used in MAMA-MIA (3D breast MRI, nnU-Net).

### Focal Loss
Variant of CE that down-weights easy examples and focuses gradients on hard pixels. Used with Dice in TDSC-ABUS (3D breast ultrasound) and Swin-UNETR implementations.

### Balanced Hybrid Loss (BCE + Dice)
Used in Bi-CBMSegNet specifically for mammography. Explicitly handles pixel-wise class imbalance between tumor and background. Achieved 97.81% Dice on INbreast — strongest mammography segmentation result found in open source.

### Multi-Task Loss Weighting
When combining segmentation + classification in one model:

L_total = λ_seg × L_seg + λ_cls × L_cls

Validated weights from caumente/multi_task_breast_cancer: λ = Dice weight, (1-λ) = Focal weight.
General validated ratio across multi-task medical imaging: λ_seg heavily dominant over λ_cls.

Why the imbalance: segmentation generates thousands of pixel gradients vs one gradient from classification. Without weighting, classification dominates and segmentation quality degrades. Heavy segmentation weighting paradoxically also improves classification by forcing the encoder to learn precise spatial features.

## From Literature / Papers
*(To be added during literature review phase)*

## Sources
→ [[Open_Sourced_Sources]]
