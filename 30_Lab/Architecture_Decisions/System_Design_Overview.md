---
type: design
status: finalized
date: 2026-03
---

# System Design Overview

Parent: [[Architecture_Decisions]]

A compressed reference of the finalized system design. For full detail see the SDD document in Submissions/.

---

## System Architecture

The system follows a modular layered architecture with a single pipeline controller coordinating all stages. One model, one forward pass, three outputs.

**Pipeline flow:**
UI button click → PipelineController.run(image_path) → PreprocessingModule.process() → MTLModel.forward() → ExplainabilityModule.generate() → UI.display() + ExportReport.create_report()

---

## Subsystems

| Subsystem | Responsibility | Input | Output |
|---|---|---|---|
| Desktop UI | Entry point, triggers pipeline, displays results | User action | Calls PipelineController |
| Pipeline Controller | Sequences and coordinates all stages, handles failures | image_path | pipeline_outputs |
| Preprocessing Module | CLAHE, pectoral mask, normalize | image_path | tensor (1, 224, 224) float32 |
| MTL Inference Model | Shared encoder → UNet++ decoder + CBAM head | tensor | mask + label + score |
| Explainability Module | Grad-CAM++ heatmap generation | tensor + model + original_image | heatmap (224, 224, 3) uint8 |
| Report Export | Serializes outputs to local report file | pipeline_outputs + output_path | report file |

**Note:** AnalysisResult is a data transfer object passed between subsystems — not an active component.

---

## Finalized Subsystem Interfaces (3.8)

**PreprocessingModule**
`process(image_path: str) → tensor: ndarray`
Returns normalized float32 array shape (1, 224, 224).

**MTLModel**
`forward(tensor: ndarray) → (mask: ndarray, label: str, score: float)`
Single forward pass. mask = uint8 (224,224), label = "Benign"/"Malignant", score = 0.0–1.0.

**ExplainabilityModule**
`generate(tensor: ndarray, model: MTLModel, original_image: ndarray) → heatmap: ndarray`
Returns color-coded overlay (224, 224, 3) uint8.

**ExportReport**
`create_report(pipeline_outputs, output_path: str) → None`

**Desktop UI**
`display(pipeline_outputs) → None`

---

## Global Control Flow

Linear, event-driven. Single "Run Analysis" trigger. No parallelism between stages. Background thread for inference to prevent UI freeze. Fail-fast — any exception halts pipeline and surfaces error to user.

---

## Key Design Decisions Summary

See full reasoning in → [[Architecture_Decision_Log]]

| Decision | Chosen | Key Reason |
|---|---|---|
| Preprocessing | MONAI + CLAHE + pectoral mask | CBIS-DDSM artifact handling |
| Segmentation | UNet++ + EfficientNet-B0 | Dice 0.929, 9M params, spiculated margins |
| Classification | Shared encoder + CBAM | MTL mutual regularization, 99.78% accuracy |
| Label mapping | Exclude BI-RADS 3 | Label ambiguity degrades decision boundary |
| Loss function | 0.7 Dice + 0.3 BCE | Seg-dominant forces morphology learning |
| Explainability | Grad-CAM++ | MGT validation, 0.29s overhead |
| Framework | PyTorch + MONAI, patient-level split | Data leakage prevention |

---

## Open Items (Implementation Phase)

- Loss weight ratio (0.7/0.3) — test 0.8/0.2 and 0.6/0.4 during training
- MGT score achievability — validate post-training against CBIS-DDSM masks
- Input resolution tradeoff — 224x224 vs 512x512 for mass boundary precision

## Sources
→ [[Open_Sourced_Sources]]
