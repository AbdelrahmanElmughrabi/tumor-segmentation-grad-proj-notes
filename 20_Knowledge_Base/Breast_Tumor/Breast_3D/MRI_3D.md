---
type: knowledge
---

# Breast MRI (3D DCE-MRI)

Parent: [[Breast_3D]]

## From Open Source Research

### What DCE-MRI Is
Dynamic Contrast-Enhanced MRI. Most sensitive imaging modality for breast cancer. Captures tissue perfusion dynamics across multiple temporal phases (pre-contrast, early post-contrast, late post-contrast). Used primarily for high-risk patients and surgical planning.

### Key Projects

**MAMA-MIA**
- Architecture: nnU-Net v2 (3d_fullres configuration)
- Dataset: 1,506 expert-annotated cases (I-SPY1, I-SPY2, Duke, NACT cohorts)
- Preprocessing: Z-score normalization across temporal phases, resampling to isotropic 1x1x1mm, NIfTI compression
- Preprocessing time: ~5 min/patient
- Input: 128x128x128 3D patches
- Loss: Dice + Cross-Entropy
- Performance: Dice 0.7620 (full image tumor segmentation)
- Pre-trained weights available on Synapse
- Gold standard benchmark for 3D breast MRI segmentation

**BreastDCEDL**
- Architecture: Vision Transformer (ViT)
- Dataset: 2,072 patient scans (I-SPY + Duke cohorts)
- Task: predicting pathological complete response (pCR) to chemotherapy
- Preprocessing: MinCrop strategy — 3 temporal phases cropped to 256x256 tumor-centered cubes
- Input: 256x256x3 (3 channels = fused temporal phases)
- Performance: AUC 0.94 for pCR prediction
- Note: focuses on treatment response prediction, not seg/class

**BreastCancerDiagnosisMRI**
- Architecture: Slice-wise CNN
- Task: detection + Grad-CAM visualization on highest-probability slice
- Input: 3 volumes (T1w post-contrast, DCE-in, DCE-out)
- Output: probability vector per sagittal slice + Grad-CAM on max probability slice
- Note: detection only, no segmentation mask

**SAM2 for MRI (Zero-shot)**
- Architecture: SAM2 with video tracking/memory logic
- Task: zero-shot segmentation — no training required
- Input: 1 bounding box on central slice → center-outward propagation
- Preprocessing: minimal, just intensity normalization
- Use case: rapid prototyping or baseline without training

### Accuracy Benchmarks
| Project | Task | Dataset | Performance |
|---|---|---|---|
| MAMA-MIA | 3D Segmentation | 1,506 cases | 0.76 Dice |
| BreastDCEDL | pCR Prediction | 2,072 cases | 0.94 AUC |

### Relevance to Our Project
MRI offers higher sensitivity than mammography but is expensive and less accessible. The MAMA-MIA nnU-Net pipeline is the most complete 3D segmentation reference available. If we ever extend beyond mammography, DCE-MRI is the highest-quality modality.

## From Literature / Papers
*(To be added during literature review phase)*

## Sources
→ [[Open_Sourced_Sources]]
