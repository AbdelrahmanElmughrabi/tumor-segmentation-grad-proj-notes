---
type: experiment
status: 🔴 Planned
date: 2026-04-16
exp_id: EXP-01
---

# EXP-01_Data_Archaeology

Parent: [[50_Experiments]]

### Objective
Conduct initial "archaeological" survey of the CBIS-DDSM dataset on Kaggle. Validate that our architectural assumptions (patient-level split, BI-RADS filtering) are executable against the raw CSV and DICOM files.

### Expected Outputs
- [ ] Patient-level 80/20 stratified split (train/test) logic.
- [ ] Counts of unique patients vs total images.
- [ ] List of resolved vs unresolved DICOM paths.
- [ ] Successful display of one raw DICOM image to verify data loading pipeline.

### Why it matters for OUR project
This is the "Ground Truth" step. If we fail to implement the patient-level split correctly now, everything downstream (validation scores, Dice coefficients) will be invalid due to data leakage.

### Risks
- DICOM paths in CSVs might not match the directory structure of the Kaggle dataset.
- BI-RADS 3 removal might reduce dataset size significantly.

### Links
- [[Architecture_Decision_Log]] — Decision 4 & 7
- [[Data_Pipeline]]
