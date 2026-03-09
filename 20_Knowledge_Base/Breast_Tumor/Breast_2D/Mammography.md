---
type: knowledge
---

# Mammography

Parent: [[Breast_2D]]

## From Open Source Research

### What Mammography Is
2D X-ray imaging of breast tissue. Primary screening modality globally. Produces grayscale images requiring specialized preprocessing due to:
- Dense breast tissue causing overlapping structures
- High noise levels requiring denoising
- Significant intensity variation across different scanner models
- DICOM format as clinical standard

### Key Preprocessing Steps Observed Across Projects
1. DICOM → JPEG/PNG conversion for DL compatibility
2. CLAHE (Contrast Limited Adaptive Histogram Equalization) for contrast enhancement
3. Gaussian blur or median filter for noise removal
4. Histogram equalization for density normalization
5. Contour-based background noise removal
6. Flipping right-sided images to face same direction (standardization)
7. Resizing to standard dimensions (512x512 common)

### Detection-Only Projects (No Segmentation)
These projects identify if/where a tumor exists via bounding boxes:

**monajemi-arman/breast_cancer_detection**
- Architectures: YOLOv8 + Faster R-CNN via Detectron2
- Datasets: InBreast, CBIS-DDSM, MIAS
- Features: Watch Folder API, DICOM converter, COCO/YOLO format support
- Preprocessing filters: Canny, CLAHE, gamma, histogram, unsharp
- Link: https://github.com/monajemi-arman/breast_cancer_detection

**Kheiron-Medical/mammo-net**
- Architecture: ResNet-18 (default), ResNet-50 (higher capacity)
- Dataset: VinDr-Mammo (20,000 images)
- Preprocessing: DICOM conversion, resize 512x512, normalization, directional flipping
- Preprocessing time: ~3 hours for 20,000 images
- Loss: Binary Cross-Entropy
- Link: https://github.com/Kheiron-Medical/mammo-net

**Batmanlab/Mammo-CLIP**
- Architecture: EfficientNet-B2/B5 (image) + BioClinicalBERT (text)
- Dataset: UPMC, VinDr-Mammo, RSNA Screening Mammography
- Unique: vision-language model, zero-shot inference via text prompts
- Loss: Multi-view supervision + contrastive alignment
- Link: https://github.com/batmanlab/Mammo-CLIP

### Segmentation + Multi-Task Projects
These projects produce pixel-level masks and/or combine segmentation with classification:

**Bi-CBMSegNet**
- Architecture: ResNet152 + GFEM (global) + LFEM (local) dual-module encoder-decoder
- Datasets: DDSM, INbreast
- Preprocessing: CLAHE, contour-based noise removal, patch extraction
- Performance: Dice 97.09% (DDSM), 97.81% (INbreast)
- Inference: ~0.8s per image
- Loss: Balanced Hybrid Loss (BCE + Dice)
- Note: No standalone repo — implemented within broader contextual modeling frameworks

**Holliemin9090/Mask R-CNN**
- Architecture: Mask R-CNN
- Task: simultaneous bounding box + segmentation mask
- Dataset: Mammographic masses
- Link: https://github.com/Holliemin9090/Mammographic-mass-CAD-via-pseudo-color-mammogram-and-Mask-R-CNN

**Ashayp31/Breast_cancer_segmentation**
- Architecture: Advanced CNN (Master's dissertation, University of St Andrews)
- Pipeline: histogram equalization + Gaussian blur → U-Net segmentation
- Documentation: clear GPU training documentation
- Link: https://github.com/Ashayp31/Breast_cancer_segmentation

### Foundation Model Reference
**VersaMammo**
- Architecture: ViT (teacher) → EfficientNet-B5 (student) via knowledge distillation
- Dataset: 706,239 images across 21 sources
- Training: 2-stage — self-supervised MIM pre-training → supervised fine-tuning
- Performance: #1 in 50/68 internal tasks, 20/24 external validation tasks
- Covers: detection, segmentation, VQA

### Accuracy Benchmarks
| Project | Task | Dataset | Dice / Accuracy |
|---|---|---|---|
| Bi-CBMSegNet | Segmentation | INbreast | 97.81% Dice |
| Bi-CBMSegNet | Segmentation | DDSM | 97.09% Dice |
| AI4BCancer (ANN) | Classification | Various | 99.12% accuracy |
| AI4BCancer (Ensemble) | Classification | Various | 97.37% accuracy |

### Known Gap
No open source project found that combines segmentation + classification + Grad-CAM in a single pipeline for 2D mammography.
See → [[Mammography_Gaps]]

## From Literature / Papers
*(To be added during literature review phase)*

## Sources
→ [[Open_Sourced_Sources]]
