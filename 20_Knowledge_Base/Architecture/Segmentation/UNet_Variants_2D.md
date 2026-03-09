---
type: knowledge
---

# U-Net Variants — 2D

Parent: [[Segmentation]]

## From Open Source Research

### Standard 2D U-Net
- Encoder (contracting) + Decoder (expanding) + Skip connections
- Skip connections preserve spatial detail lost during max-pooling downsampling
- Each encoder block: Conv → BatchNorm → ReLU → Conv → BatchNorm → ReLU → MaxPool
- Each decoder block: Upsample → Concat(skip) → Conv → Conv
- Final: 1x1 Conv + Sigmoid/Softmax for pixel-wise prediction

### 2D Multi-Task U-Net (Most Relevant to Our Project)
Shared encoder splits at bottleneck into two branches:
1. Segmentation decoder — reconstructs pixel-wise mask via skip connections
2. Classification head — GAP → Dense → Dropout → output

The closest open source implementation of this pattern for breast imaging is caumente/multi_task_breast_cancer (ultrasound, U-Net++, BUSI dataset). No combined multi-task U-Net for mammography specifically has been found yet — see [[Mammography_Gaps]] GAP-01.

### U-Net++ (Nested Skip Connections)
- Adds dense skip connections between encoder and decoder at multiple scales
- Bridges semantic gap between encoder and decoder features more effectively
- Used in caumente/multi_task_breast_cancer for breast ultrasound
- Better for small or irregular tumors

### ResNet Encoder U-Net
- Replaces standard encoder blocks with pre-trained ResNet (ResNet-34, ResNet-50)
- Transfer learning from ImageNet gives stronger feature initialization
- Used in Kheiron-Medical/mammo-net for mammography classification
- Trade-off: faster convergence, less architectural control

### Mask R-CNN (Detection + Segmentation)
- Extends Faster R-CNN with a segmentation mask branch
- Simultaneously outputs bounding box + pixel mask
- Used in Holliemin9090 mammography project
- Not end-to-end with classification — separate task from benign/malignant prediction

### Accuracy Benchmarks (Breast Projects)
| Implementation | Modality | Task | Performance |
|---|---|---|---|
| Bi-CBMSegNet | Mammography | Segmentation | 97.81% Dice (INbreast) |
| Bi-CBMSegNet | Mammography | Segmentation | 97.09% Dice (DDSM) |
| caumente MTL | Ultrasound | Seg + Class | Dice + Focal (BUSI) |
| DenseNet121 | Ultrasound | Classification | 3-class (BUSI) |

Note: no combined seg+class mammography benchmark found yet — establishing this is part of our project's contribution.

## From Literature / Papers
*(To be added during literature review phase)*

## Sources
→ [[Open_Sourced_Sources]]
