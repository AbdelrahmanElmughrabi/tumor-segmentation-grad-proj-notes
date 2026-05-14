---
type: experiment
status: completed
date: 2026-05
parent: Experiment_Series_05
---
# EXP05_05: Run 5.3 (Mass-Only + Aug + Focal Loss)

## Goal
Implement a highly optimized training strategy to maximize Dice performance and eliminate the massive overfitting gap observed in the baseline.

## What Was Done
* **Filtering**: Applied Mass-only filter in EXP01 (dropped all calcification cases).
* **Augmentation**: Added `RandFlip` and `RandRotate` (up to 15°) to the training pipeline.
* **Loss Function**: Replaced standard BCE with `Focal Loss` (γ=2.0, α=0.25) to handle class imbalance.
* **XAI Fix**: Updated Grad-CAM++ target layer to `blocks[-1][-1]` for better feature resolution.

## Outcomes
* ✅ **Test Dice**: 0.506 (+122% vs baseline, tied with Run 5.2).
* ⚠️ **Test AUC**: 0.757 (-3% vs baseline, but +10% vs Run 5.2).
* ✅ **Overfitting Gap**: 0.07 (Dramatically reduced from 0.47).
* ✅ **Key Win**: Mass-only filtering alone added +278 Dice points.

## In Plain Words
By focusing only on masses and teaching the AI to be more flexible (rotations/flips), we nearly cured the "overfitting" problem where the AI just memorized the training images. The model is now much more stable and generalizes well, though it's still hitting a "ceiling" when trying to find tiny tumors in large images.

## Current Status
This is the most stable model to date. It has the best generalization and has recovered most of the classification performance lost in Run 5.2, while keeping the high Dice score.

Parent: [[Experiment_Series_05]]