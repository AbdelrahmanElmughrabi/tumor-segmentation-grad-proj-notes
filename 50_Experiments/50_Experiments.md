---
type: nexus
status: in-progress
date: 2026-03
---
# 50_Experiments: Technical Lab & Training Runs

Project: Breast Tumor Detection — CBIS-DDSM
Team: Abdelrahman Elmughrabi (21SOFT1070), Dilara Sönmez (20COMP1015)

## Overview
This folder contains the technical execution of the project, organized into sequential training series. Each series represents a full iteration of the pipeline with specific architectural or strategic modifications.

## Experiment Series Master Index
| Series | Date | Primary Goal | Key Outcome | Status |
| :--- | :--- | :--- | :--- | :--- |
| [[Experiment_Series_01]] | 2026-03 | Baseline Pipeline | established metrics; high overfitting | ✅ |
| [[Experiment_Series_02]] | 2026-03 | Mixed Perspective (Crops) | Identified Mask Alignment Trap | ✅ |
| [[Experiment_Series_03]] | 2026-04 | Mass-Only Optimization | Dice doubled (0.50); overfitting closed | ✅ |
| [[Experiment_Series_04]] | 2026-04 | Staged Training | Halved False Positives; high-res Grad-CAM | ✅ |

## Workflow
1. **Data Prep** (EXP01) → **Standardization** (EXP02) → **Model Build** (EXP03)
2. **Stability Check** (EXP04) → **Full Scale Training** (EXP05) → **Explainability** (EXP06)

Parent: [[Project_MOC]]