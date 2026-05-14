---
type: experiment
status: completed
date: 2026-05
parent: Experiment_Series_05
---
# EXP04_05: Strategy Optimization

## Goal
Define the training strategy for the Series 05 optimization run, focusing on data variety and loss stability.

## What Was Done
* **Augmentation**: Integrated MONAI `RandFlipd` and `RandRotated` (range 0.26 rad) into the `train_transforms`.
* **Classification Loss**: Configured `BinaryFocalLoss` with $\gamma=2.0$ and $\alpha=0.25$ to force the model to focus on "hard" samples.
* **Combined Loss**: Maintained the MTL balance: $0.7 \times \text{Dice} + 0.3 \times \text{Focal}$.

## Outcomes
* ✅ Effectively reduced overfitting gap to 0.07.
* ✅ Stabilized the classification branch during MTL training.

Parent: [[Experiment_Series_05]]