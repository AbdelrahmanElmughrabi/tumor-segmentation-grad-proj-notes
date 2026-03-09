---
type: comparison
---

# 2D Pipelines Comparison

Parent: [[Breast_2D]]

Each column represents a pipeline stage. `—` means that stage is not covered by the project.

---

## Mammography

| Project | Dataset | Detection | Segmentation | Classification | Explainability | Repo |
|---|---|---|---|---|---|---|
| monajemi-arman/breast_cancer_detection | InBreast, CBIS-DDSM, MIAS | YOLOv8 + Faster R-CNN | — | — | — | [Link](https://github.com/monajemi-arman/breast_cancer_detection) |
| Kheiron-Medical/mammo-net | VinDr-Mammo (20k) | ResNet-18/50 | — | Binary (BCE) | — | [Link](https://github.com/Kheiron-Medical/mammo-net) |
| batmanlab/Mammo-CLIP | UPMC, VinDr-Mammo, RSNA | EfficientNet-B2/B5 | — | Zero-shot via text prompt | — | [Link](https://github.com/batmanlab/Mammo-CLIP) |
| Holliemin9090/Mask R-CNN | Mammographic masses | Faster R-CNN | Mask R-CNN | — | — | [Link](https://github.com/Holliemin9090/Mammographic-mass-CAD-via-pseudo-color-mammogram-and-Mask-R-CNN) |
| Ashayp31/Breast_cancer_segmentation | Mammography | — | U-Net | — | — | [Link](https://github.com/Ashayp31/Breast_cancer_segmentation) |
| Bi-CBMSegNet | DDSM, INbreast | — | ResNet152 + Dual-module decoder (97.81% Dice) | — | — | No standalone repo |

---

## Ultrasound

| Project | Dataset | Detection | Segmentation | Classification | Explainability | Repo |
|---|---|---|---|---|---|---|
| caumente/multi_task_breast_cancer | BUSI (curated) | — | U-Net++ shared backbone | Shared encoder head | — | [Link](https://github.com/caumente/multi_task_breast_cancer) |
| m3mentomor1/DenseNet121 | BUSI | — | — | DenseNet121 (3-class) | — | [Link](https://github.com/m3mentomor1/Breast-Cancer-Image-Classification-with-DenseNet121) |

---

## Gap Summary

| Segmentation | Classification | Explainability | Modality | Exists? |
|---|---|---|---|---|
| ✅ | — | — | Mammography | ✅ Multiple |
| — | ✅ | — | Mammography | ✅ Multiple |
| ✅ | ✅ | — | Ultrasound | ✅ caumente |
| ✅ | ✅ | ✅ | Any | ❌ Nobody |
| ✅ | ✅ | ✅ | Mammography | ❌ Nobody |

See → [[Mammography_Gaps]]

## Sources
→ [[Open_Sourced_Sources]]
