---
type: brainstorm
---

# Architecture Considerations

Parent: [[Architecture_Decisions]]

Open considerations — not yet final decisions. To be discussed with teammate and updated as research progresses.

## Modality
Mammography (2D) confirmed as primary.
3D (DBT) remains in perspective as a potential extension.

## 2D vs 3D
**2D:** simpler pipeline, faster iteration, mammography is natively 2D, more open source references available.
**3D (DBT):** volumetric context, better accuracy potential, but higher compute cost and fewer references. Feasibility unclear — see [[Mammography_Gaps]] GAP-06.

Current thinking: start 2D, evaluate 3D as upgrade path.

## Architecture Pattern
Multi-task U-Net (shared encoder + segmentation decoder + classification head) is the established pattern for combined seg+class. caumente/multi_task_breast_cancer is the closest breast-specific open source reference using U-Net++ with a shared backbone on ultrasound. No mammography-specific multi-task implementation found yet — see [[Mammography_Gaps]] GAP-01.

Open questions:
- Standard U-Net encoder vs pretrained ResNet encoder?
- U-Net vs U-Net++ for segmentation decoder?
- Binary classification (benign/malignant) vs multi-class (BI-RADS categories)?

## Framework
PyTorch + MONAI is the strongest choice based on ecosystem, medical imaging support, and Grad-CAM library compatibility.

## Explainability
Grad-CAM is the standard. Seg-Grad-CAM adaptation needed for the segmentation branch. BreastCancerDiagnosisMRI applies Grad-CAM to breast MRI per slice — closest breast-specific explainability reference found. No mammography-specific Grad-CAM reference found — see [[Mammography_Gaps]] GAP-02.

## Dataset
Pending. See [[Mammography_Gaps]] GAP-03.
Candidates: CBIS-DDSM, INbreast, VinDr-Mammo.
