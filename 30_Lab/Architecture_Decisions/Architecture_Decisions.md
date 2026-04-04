---
type: nexus
---

# Architecture Decisions

Finalized decisions on system design. Each note should document: what we chose, what we rejected, and why.

Parent: [[Lab]]

## Decision Log
| Decision       | Chosen                        | Rejected          | Reason                                     | Date    |
| -------------- | ----------------------------- | ----------------- | ------------------------------------------ | ------- |
| Preprocessing  | MONAI (CLAHE + Pectoral Mask) | Global Hist. Eq.  | Noise/artifact handling in CBIS-DDSM       | 2026-03 |
| Segmentation   | UNet++ (EfficientNet-B0)      | Standard U-Net    | Better handling of spiculated mass margins | 2026-03 |
| Classification | Shared Encoder + CBAM         | Separate Backbone | MTL mutual regularization & attention      | 2026-03 |
| Label Mapping  | Exclude BI-RADS 3             | Include as Benign | Removes label ambiguity/uncertainty        | 2026-03 |
| Explainability | Grad-CAM++                    | SHAP / LIME       | Clinical consistency & spatial precision   | 2026-03 |

## Notes Index
- [[Pipeline_Decisions_CBIS_DDSM]] — Full detailed log for the Mammography AI Pipeline.
 
