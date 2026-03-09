---
type: knowledge
---

# Digital Breast Tomosynthesis (DBT)

Parent: [[Breast_3D]]

## From Open Source Research

### What DBT Is
Advanced form of mammography. Takes multiple X-ray images from different angles and reconstructs a 3D volume. Significantly reduces the impact of overlapping tissue that obscures tumors in standard 2D mammography.

Produces: sequence of reconstructed slices (similar to CT) rather than a single projection.

### Challenges
- Very high resolution volumes (up to 1.63TB for large datasets)
- Requires 3D CNNs or slice-sequence processing
- Specialized preprocessing pipeline

### Key Projects

**TomoLIBRA**
- Framework: GaNDLF (Generally Nuanced Deep Learning Framework)
- Architecture: 3D CNN
- Task: Volumetric Breast Density (VBD) estimation + tissue segmentation
- Dataset: Breast Cancer Screening DBT dataset (22,032 samples, 5,000+ subjects)
- Preprocessing: standardized via preprocess_images.py script
- Hardware: requires NVIDIA CUDA 11.8/12.2, supports multi-GPU
- Use case: tissue density analysis for cancer risk assessment

**priyak307/Breast-Cancer-Screening-DBT**
- Frameworks: Detectron2 + Faster R-CNN + YOLOv8
- Task: lesion detection within 3D DICOM volumes
- Focus: distinguishing benign from malignant across hundreds of slices automatically

### Accuracy Benchmarks
| Project | Task | Performance |
|---|---|---|
| TomoLIBRA | VBD Segmentation | Benchmark on 1.63TB dataset |

### Relevance to Our Project
DBT is a natural evolution of mammography. If our 2D mammography pipeline proves successful, DBT is a logical upgrade path — same modality, added volumetric context. Architecture would shift from 2D U-Net to 3D CNN processing reconstructed slices.

## From Literature / Papers
*(To be added during literature review phase)*

## Sources
→ [[Open_Sourced_Sources]]
