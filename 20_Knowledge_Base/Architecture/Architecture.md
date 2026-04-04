---
type: nexus
---

# Architecture

Parent: [[Knowledge_Base]]

## Sub-sections
- [[Segmentation]] — U-Net variants, loss functions, normalization
- [[Classification]] — Multi-task patterns, classification head design
- [[Explainability]] — Grad-CAM, Seg-Grad-CAM, heatmap interpretation

## Notes
Architecture notes here are modality-agnostic — the patterns apply across medical imaging tasks. Breast-specific architectural observations are in [[Breast_Tumor]].

See current architectural thinking → [[Architecture_Considerations]]

## Sources
→ [[Open_Sourced_Sources]]

## Finalized Architecture (March 2026)

After CBIS-DDSM specific research and SDD design phase, the following stack was finalized:

- **Encoder:** EfficientNet-B0 (pretrained ImageNet, shared across both tasks)
- **Segmentation decoder:** UNet++ with nested dense skip connections
- **Classification head:** CBAM + GAP → Dense(256) → Dropout(0.5) → Dense(1) → Sigmoid
- **Explainability:** Grad-CAM++ hooked to final encoder conv layer (post-inference)
- **Framework:** PyTorch + MONAI
- **Dataset:** CBIS-DDSM, patient-level 80/20 split, batch 16 at 224x224

See full system design → [[System_Design_Overview]]
See full decision reasoning → [[Architecture_Decision_Log]]
