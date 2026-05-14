---
type: experiment
status: completed
date: 2026-05
parent: Experiment_Series_05
---
# EXP05_05: Run 5.2 (Recovered Model)

## Goal
Restore and evaluate an earlier training checkpoint that demonstrated superior visual localization during monitoring.

## What Was Done
* Recovered model state from a specific earlier epoch checkpoint.
* Evaluated against the full test set to establish benchmark metrics for this "visually superior" state.

## Outcomes
* ✅ **Test Dice**: 0.506 (+122% vs baseline).
* ⚠️ **Test AUC**: 0.655 (-13% vs baseline).
* ✅ **Overfitting**: Better controlled than the baseline run.
* ✅ **Visual Quality**: Superior heatmap precision and more accurate tumor localization visually.

## In Plain Words
Numbers don't tell the whole story. While this version "scored" lower on classification (AUC), it is much better at actually finding and drawing the tumor correctly. It's a better candidate for real-world use than the models that just guess the label correctly without showing their work.

## Key Finding
Numerical metrics and visual quality can diverge significantly. This model shows that high spatial alignment can exist even when classification scores dip.

Parent: [[Experiment_Series_05]]