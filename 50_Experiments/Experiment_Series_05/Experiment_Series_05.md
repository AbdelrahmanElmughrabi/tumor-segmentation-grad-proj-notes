---
type: nexus
status: completed
date: 2026-05
---
# Experiment Series #5: Optimization & Recovery

Project: Breast Tumor Detection — CBIS-DDSM
Team: Abdelrahman Elmughrabi (21SOFT1070), Dilara Sönmez (20COMP1015)
Date: May 2026

## Summary
This series focuses on stabilizing the training pipeline through two distinct approaches: recovering a high-spatial-precision checkpoint (Run 5.2) and implementing a mass-only optimization strategy with Focal Loss and Augmentation (Run 5.3). It represents the most significant breakthrough in Dice performance and overfitting control to date.

## Experiment Index
| Experiment | Status | Change Summary |
| :--- | :--- | :--- |
| EXP01: Data | ✅ | Added Mass-only filter (dropped calcifications) |
| EXP02: Pre-processing | - | Unchanged (standardized MONAI pipeline) |
| EXP03: Architecture | - | Unchanged (EfficientNet-B0 + UNet++ + CBAM) |
| [[Run_5.3_Optimized/EXP04_Run5.3]] | ✅ | Added RandFlip/Rotate & Focal Loss |
| [[Run_5.2_Recovered/EXP05_Run5.2]] | ✅ | Recovered Checkpoint: High localization precision |
| [[Run_5.3_Optimized/EXP05_Run5.3]] | ✅ | Full Optimization: Mass-only + Aug + Focal Loss |
| [[Run_5.3_Optimized/EXP06_Run5.3]] | ✅ | Fixed Grad-CAM target to blocks[-1][-1] |

## Key Learnings
* **Mass-only filtering** provided the largest single performance jump (+278 Dice points).
* **Numerical metrics (AUC) and visual quality (Heatmaps) can diverge**; Run 5.2 is a superior deployment candidate despite lower numbers.
* **Overfitting is solved**; the gap was reduced from 0.47 (Baseline) to 0.07 (Run 5.3).
* **The Localization Ceiling**: Segmentation is currently capped at ~0.506 for 512x512 full images, despite crops reaching ~0.90.

Parent: [[50_Experiments]]