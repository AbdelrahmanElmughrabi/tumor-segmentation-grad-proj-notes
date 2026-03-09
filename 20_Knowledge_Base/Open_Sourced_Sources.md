---
type: reference
---

# Open Sourced Sources

Parent: [[Knowledge_Base]]

Master credits file. All KB notes point here. Organized by source type.

---

## Deep Research Reports (Gemini Deep Search)

**[S1]** "Technical Evaluation of Open-Source Computational Frameworks for Multi-Dimensional Breast Tumor Detection, Segmentation, and Classification"
Covers: 2D/3D breast tumor projects across mammography, ultrasound, MRI, DBT — architectures, pipelines, preprocessing, evaluation metrics, data formats.
Informed: [[Mammography]], [[Ultrasound_2D]], [[MRI_3D]], [[DBT]], [[Ultrasound_3D]], [[Frameworks_Landscape]], [[Data_Formats]]

---

## Key Papers

**[P1]** Ronneberger et al. "U-Net: Convolutional Networks for Biomedical Image Segmentation." MICCAI 2015.
Core architecture reference — foundational to all segmentation pipelines.

---

## GitHub Repositories

**[G1]** jacobgil/pytorch-grad-cam
Standard Grad-CAM library for PyTorch. Used for explainability integration.

**[G2]** Project-MONAI/tutorials
https://github.com/Project-MONAI/tutorials
Medical imaging framework. BraTS and TCIA dataset examples — framework reference only, not breast-specific.

**[G3]** caumente/multi_task_breast_cancer
https://github.com/caumente/multi_task_breast_cancer
Best open source reference for combined seg+class on breast imaging (ultrasound).

**[G4]** monajemi-arman/breast_cancer_detection
https://github.com/monajemi-arman/breast_cancer_detection
Most complete mammography detection pipeline open source.

**[G5]** Kheiron-Medical/mammo-net
https://github.com/Kheiron-Medical/mammo-net
ResNet classification on VinDr-Mammo. Preprocessing pipeline reference.

**[G6]** batmanlab/Mammo-CLIP
https://github.com/batmanlab/Mammo-CLIP
Vision-language model for mammography. Foundation model awareness.

**[G7]** Ashayp31/Breast_cancer_segmentation
https://github.com/Ashayp31/Breast_cancer_segmentation
U-Net segmentation on mammography with clean GPU training documentation.

**[G8]** m3mentomor1/DenseNet121
https://github.com/m3mentomor1/Breast-Cancer-Image-Classification-with-DenseNet121
DenseNet121 classification on BUSI. Streamlit deployment reference.

**[G9]** BreastCancerDiagnosisMRI
Grad-CAM applied to breast DCE-MRI per slice. Explainability pattern reference.
