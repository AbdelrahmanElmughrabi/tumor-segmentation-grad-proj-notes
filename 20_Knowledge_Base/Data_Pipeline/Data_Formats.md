---
type: knowledge
---

# Data Formats

Parent: [[Data_Pipeline]]

## From Open Source Research

### DICOM
Clinical standard. Used by hospitals and scanners. Contains image pixels + extensive patient metadata. Requires conversion for most DL pipelines.
Tools: SimpleITK, pydicom, MONAI transforms, dedicated conversion scripts.

### NIfTI (.nii / .nii.gz)
Standard for 3D medical imaging research. Used by BraTS and breast MRI datasets (MAMA-MIA, BreastDCEDL). Loaded via `nibabel` in Python. Stores volumetric array + affine transformation matrix.

### JPEG / PNG
Used after DICOM conversion for 2D mammography pipelines. Compatible with standard DL libraries directly. No spatial metadata preserved.

### HDF5
High-performance binary format for preprocessed arrays. Used to significantly accelerate data loading during training (parallel access, compressed storage). Convert once during preprocessing, load fast during every training epoch.

### NRRD
Used in ABUS (3D ultrasound) pipelines. Similar to NIfTI for volumetric data, loaded directly in PyTorch dataset wrappers.

### Practical Notes for Our Project
- Mammography input likely arrives as DICOM → convert to JPEG/PNG for 2D pipeline
- If extending to 3D or MRI → NIfTI is the target format
- Consider HDF5 for storing preprocessed slices if dataset is large

## From Literature / Papers
*(To be added during literature review phase)*

## Sources
→ [[Open_Sourced_Sources]]
