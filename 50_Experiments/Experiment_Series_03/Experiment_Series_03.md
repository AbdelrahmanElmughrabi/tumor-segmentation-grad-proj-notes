---
type: nexus
status: completed
date: 2026-04
---
# Experiment Series #3: Mass-Only Optimization

Project: Breast Tumor Detection — CBIS-DDSM
Team: Abdelrahman Elmughrabi (21SOFT1070), Dilara Sönmez (20COMP1015)
Date: April 2026

## Summary
Focused optimization targeting Mass cases only. Introduced augmentation and Focal Loss to combat overfitting and class imbalance.

## Experiment Index
| Experiment | Status | Change Summary |
| :--- | :--- | :--- |
| [[EXP01_03]] | ✅ | Added Mass-only filter (dropped calcifications) |
| EXP02: Unchanged | - | Preprocessing pipeline remains stable |
| EXP03: Unchanged | - | Model architecture remains same |
| [[EXP04_03]] | ✅ | Added RandFlip + RandRotate augmentations |
| [[EXP05_03]] | ✅ | Replaced BCE with Focal Loss; Dice doubled |
| [[EXP06_03]] | ✅ | Fixed target layer to blocks[-1][-1] |

Parent: [[50_Experiments]]