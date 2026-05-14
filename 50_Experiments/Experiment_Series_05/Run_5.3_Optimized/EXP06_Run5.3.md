---
type: experiment
status: completed
date: 2026-05
parent: Experiment_Series_05
---
# EXP06_05: Explainability Fix

## Goal
Improve the spatial resolution of heatmaps by targeting a deeper, more feature-rich layer in the EfficientNet-B0 encoder.

## What Was Done
* **Layer Targeting**: Re-hooked Grad-CAM++ from the generic `blocks[-1]` to the specific `blocks[-1][-1]` sub-module.
* **Verification**: Ran comparison heatmaps on 10 validation samples.

## Outcomes
* ✅ Heatmaps now align more tightly with the actual ROI boundaries.
* ✅ Visual confirmation of "The Localization Bottleneck" (AI is looking at the right area but not drawing fine edges).

Parent: [[Experiment_Series_05]]