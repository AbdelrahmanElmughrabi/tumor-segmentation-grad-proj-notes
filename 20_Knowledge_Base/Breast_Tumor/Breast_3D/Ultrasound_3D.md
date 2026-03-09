---
type: knowledge
---

# Automated Breast Ultrasound (ABUS)

Parent: [[Breast_3D]]

## From Open Source Research

### What ABUS Is
Automated 3D Breast Ultrasound. Standardized alternative to handheld ultrasound — provides multi-angle volumetric evaluations. Reduces operator dependency of traditional ultrasound.

Challenges: variable tumor size, low signal-to-noise ratio, high variability in acquisition.

### Key Projects

**TDSC-ABUS Challenge Codebase**
- Architectures: 3D UNet++, Swin-UNETR, STU-NET
- Dataset: TDSC-ABUS 2023 (200 volumes, Invenia ABUS system)
- Format: .nrrd files, voxel-level radiologist annotations
- Input dimensions: 843x546x270 to 865x682x354 (variable)
- Loss: Weighted Dice + Focal Loss (handles extreme class imbalance)
- State of the art for 3D ABUS tumor boundary delineation

**abus-classification**
- Framework: PyTorch
- Task: lesion classification using texture + vascular + shape features
- Dataset: IIPL-3D-ABUS (restricted, lab-internal)
- License: MIT

**Flip Learning (Weakly Supervised)**
- Method: Multi-Agent Reinforcement Learning + Curriculum Learning
- Task: hybrid segmentation + classification
- Performance: Dice 75.5% on ABUS nodules with fewer labels than fully supervised

### Accuracy Benchmarks
| Project | Task | Performance |
|---|---|---|
| 3D UNet++ (TDSC) | Segmentation | State of the art for ABUS |
| Flip Learning | Seg + Class | 75.5% Dice |

### Relevance to Our Project
ABUS is a different modality from mammography. Relevant mainly as an architecture reference — 3D UNet++ nested skip connections are an interesting upgrade from standard U-Net for small irregular tumor detection.

## From Literature / Papers
*(To be added during literature review phase)*

## Sources
→ [[Open_Sourced_Sources]]
