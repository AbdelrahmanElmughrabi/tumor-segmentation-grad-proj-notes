---
type: nexus
status: completed
date: 2026-04
---
# Experiment Series #4: Staged Training & Tversky

Project: Breast Tumor Detection — CBIS-DDSM
Team: Abdelrahman Elmughrabi (21SOFT1070), Dilara Sönmez (20COMP1015)
Date: April 2026

## Summary
Final refinement using staged training to isolate segmentation learning and Tversky loss to penalize false negatives.

## Experiment Index
| Experiment | Status | Change Summary |
| :--- | :--- | :--- |
| EXP01: Unchanged | - | Mass-only filtering preserved |
| EXP02: Unchanged | - | Preprocessing remains stable |
| EXP03: Unchanged | - | Model remains same |
| [[EXP04_04]] | ✅ | Implemented Staged Training (Phase 1 Seg-only) |
| [[EXP05_04]] | ✅ | Replaced Dice with Tversky; Halved False Positives |
| [[EXP06_04]] | ✅ | Target layer moved to blocks[-2][-1] for res |

Parent: [[50_Experiments]]