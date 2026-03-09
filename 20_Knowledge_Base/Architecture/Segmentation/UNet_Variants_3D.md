---
type: knowledge
---

# U-Net Variants — 3D

Parent: [[Segmentation]]

## From Open Source Research

### Standard 3D U-Net
Replaces all 2D convolutions with 3D volumetric convolutions. Captures inter-slice spatial context that 2D misses.

Memory requirement: ~3150MB base (vs ~180MB for 2D U-Net) — ~20x increase.
Requires patch-based training on 16GB VRAM hardware.

### Pocket U-Net
Challenges the convention that filter count must double after each pooling layer. Keeps filters minimal throughout.
- Parameters: 0.1M (vs 41.5M standard)
- Peak VRAM: 4.8GB (vs 15.3GB standard)
- Performance: statistically identical to full U-Net
- Best choice for constrained hardware

### ResUNet (3D)
Adds residual connections within encoder/decoder blocks.
- Helps gradient flow in deep networks
- Slightly faster per epoch due to compiler optimizations on identity paths
- Requires more epochs to converge

### Attention U-Net (3D) — Avoid on Limited Hardware
Adds self-attention gates to suppress background and focus on tumor regions.
- Theoretically stronger for class imbalance
- Computationally catastrophic in 3D: attention scales quadratically with volume
- Avoid unless running on multi-GPU cluster

### nnU-Net
Self-configuring framework. Analyzes dataset and auto-configures everything.
- Automatically sets patch size, normalization, architecture depth
- Uses Instance Normalization by default
- Strong baseline but not easily adapted for multi-task learning

### 3D vs 2D Tradeoff Summary
| Factor | 2D | 3D |
|---|---|---|
| Inter-slice context | ❌ Lost | ✅ Captured |
| Memory (16GB VRAM) | ✅ Comfortable | ⚠️ Tight, needs patches |
| Iteration speed | ✅ Fast | ⚠️ Slower per run |
| Dice scores | Lower | Higher |
| Thesis strength | Acceptable | Stronger |
| Batch Normalization | ✅ Works | ❌ Replace with Instance Norm |

### Accuracy Benchmarks (3D on BraTS — Reference Only)
| Architecture | Hardware | Dice WT | Dice TC | Dice ET |
|---|---|---|---|---|
| Full 3D U-Net | T4 | 0.916 | 0.841 | 0.763 |
| Pocket U-Net | T4 | 0.915 | 0.838 | 0.771 |
| 3D U-Net (A100) | A100 | 0.901 | 0.887 | 0.881 |
| MAMA-MIA nnU-Net | Multi-GPU | 0.762 | N/A | N/A |

Note: BraTS benchmarks are brain MRI — included as architectural reference only. Breast mammography benchmarks to be established.

## From Literature / Papers
*(To be added during literature review phase)*

## Sources
→ [[Open_Sourced_Sources]]
