---
type: nexus
status: completed
date: 2026-03
---
# Experiment Series #2: Mixed Dataset (Crop Strategy)

Project: Breast Tumor Detection — CBIS-DDSM
Team: Abdelrahman Elmughrabi (21SOFT1070), Dilara Sönmez (20COMP1015)
Date: March 2026

## Summary
An attempt to improve localization and texture learning by doubling the dataset with cropped images. This series identified the "Mask Alignment Trap."

## Experiment Index
| Experiment | Status | Change Summary |
| :--- | :--- | :--- |
| [[EXP01_02]] | ✅ | Linked Crop_Path to each patient row |
| [[EXP02_02]] | ✅ | Added CROP tag logic to bypass pectoral removal |
| EXP03: Unchanged | - | Architecture remains compatible |
| [[EXP04_02]] | ✅ | Implemented MixedCBISDDSMDataset logic |
| [[EXP05_02]] | ✅ | Results: Metrics drop due to mask misalignment |
| EXP06: Unchanged | - | Explainability baseline remains same |

Parent: [[50_Experiments]]