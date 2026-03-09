---
type: knowledge
---

# Preprocessing

Parent: [[Data_Pipeline]]

## From Open Source Research

### Mammography Preprocessing (2D)
Observed across open source mammography projects:

1. DICOM → JPEG/PNG conversion
2. CLAHE (Contrast Limited Adaptive Histogram Equalization) for contrast enhancement
3. Gaussian blur or median filter for noise removal
4. Histogram equalization for scanner normalization
5. Contour-based background noise removal
6. Directional standardization (flip right-sided images to face same direction)
7. Resize to standard dimensions (512x512 common)

No consensus on optimal ordering or which steps are mandatory for combined seg+class tasks. See [[Mammography_Gaps]] GAP-05.

### MRI Preprocessing (Reference)
Standard for BraTS/DCE-MRI:
1. Z-score normalization on foreground brain/tissue region only
2. N4ITK bias field correction (removes magnetic field inhomogeneities)
3. Intensity clipping (top/bottom 1%) to remove artifacts
4. Resampling to isotropic voxel spacing
5. Patch extraction (128x128x128 for 3D)

### 3D Patch Extraction
For 3D models that cannot fit full volumes in VRAM:
- Standard patch size: 128x128x128
- Must be divisible by 2^N (N = number of pooling layers)
- Random patch sampling during training, sliding window during inference
- Alternative sizes: 96x160x160, 96x96x96 for tighter memory

### Class Imbalance Handling
Tumor pixels are vastly outnumbered by background:
- Filter slices/patches with no tumor content during data loading
- Use Dice Loss instead of Cross-Entropy (handles imbalance mathematically)
- Oversampling tumor-containing patches during training

## From Literature / Papers
*(To be added during literature review phase)*

## Sources
→ [[Open_Sourced_Sources]]
