---
type: knowledge
---

# Ultrasound 2D

Parent: [[Breast_2D]]

## From Open Source Research

### What Breast Ultrasound Is
Complementary modality to mammography. Particularly useful for:
- Dense breast tissue where mammography has lower sensitivity
- Distinguishing solid masses from fluid-filled cysts
- Point-of-care settings (POCUS)

Primary dataset: BUSI (Breast Ultrasound Images) — women aged 25-75, 3 classes: normal, benign, malignant.

### Classification Projects

**m3mentomor1/DenseNet121**
- Architecture: DenseNet121 with ImageNet transfer learning
- Dataset: BUSI
- Task: 3-class classification (normal, benign, malignant)
- Input: 224x224 (standard DenseNet input)
- Parameters: 68.7M trainable
- Loss: Categorical Cross-Entropy, Adam optimizer
- Deployment: Streamlit web app for browser-based testing
- Link: https://github.com/m3mentomor1/Breast-Cancer-Image-Classification-with-DenseNet121

### Multi-Task Projects (Segmentation + Classification)

**caumente/multi_task_breast_cancer**
- Architecture: Shared backbone (U-Net++ or nnU-Net) → dual branches
- Dataset: BUSI + "Curated BUSI" (330 duplicates removed to prevent data leakage)
- Task: simultaneous segmentation + classification
- Loss: L_total = λ * L_dice + (1-λ) * L_focal
- Unique contribution: data curation removing duplicates — more reliable metrics
- Link: https://github.com/caumente/multi_task_breast_cancer

### Accuracy Benchmarks
| Project | Task | Dataset | Performance |
|---|---|---|---|
| DenseNet121 | Classification | BUSI | 3-class (benign/malignant/normal) |
| caumente MTL | Seg + Class | Curated BUSI | Multi-task Dice + focal loss |

### Notes on Ultrasound vs Mammography for Our Project
Ultrasound is natively 2D and simpler to preprocess than mammography. However our project targets mammography. Ultrasound projects are useful as architectural references for multi-task patterns — especially caumente which is the closest open source match to our combined pipeline concept.

## From Literature / Papers
*(To be added during literature review phase)*

## Sources
→ [[Open_Sourced_Sources]]
