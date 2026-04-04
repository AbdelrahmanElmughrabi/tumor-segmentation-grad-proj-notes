---
type: gaps
---

# Mammography Gaps

Parent: [[Gaps]]

Known gaps in our understanding of the 2D mammography pipeline. Prioritized by how directly they block our project.

## Critical Gaps (Block Architecture Decision)

**GAP-01: No open source combined pipeline found**
No public project combines segmentation + classification + Grad-CAM in a single end-to-end pipeline specifically for 2D mammography. The closest match (caumente/multi_task_breast_cancer) does segmentation + classification on ultrasound, not mammography.
- Status: ✅ Closed — designed in SDD March 2026. See [[System_Design_Overview]]
- Why it matters: we are building something that doesn't exist cleanly in open source — confirms novelty but means no direct reference implementation

**GAP-02: Mammography-specific Grad-CAM integration**
Grad-CAM has been applied to MRI (BreastCancerDiagnosisMRI) and general classification CNNs. No open source reference found applying Seg-Grad-CAM to a 2D mammography segmentation model.
- Status: 🔴 Open
- Why it matters: implementation will require adapting from brain MRI or general medical imaging references

**GAP-03: Dataset decision pending**
Mammography dataset not yet finalized. Candidates from research: CBIS-DDSM, INbreast, VinDr-Mammo. Each has different format, size, and annotation quality.
- Status: 🔴 Open
- Why it matters: dataset choice affects preprocessing pipeline, class distribution, and achievable Dice benchmarks

## Secondary Gaps (Need Research)

**GAP-04: Benign/malignant label availability in mammography datasets**
Unlike BraTS (LGG/HGG split) or BUSI (explicit benign/malignant labels), mammography datasets use BI-RADS scores. Need to understand how BI-RADS maps to benign/malignant for our classification branch.
- Status: 🔴 Open

**GAP-05: Mammography-specific preprocessing standards**
Breast MRI uses Z-score normalization. Mammography uses CLAHE + histogram equalization. No clear consensus found on the best preprocessing pipeline for combined seg+class tasks on mammography.
- Status: 🔴 Open

**GAP-06: 3D mammography (DBT) feasibility on our hardware**
DBT compute requirements not benchmarked for our specific hardware budget. TomoLIBRA requires multi-GPU. Unknown if single T4/A100 is sufficient for any meaningful DBT training run.
- Status: 🟡 Partially open — needs smoke test

## Resolved Gaps
*(Move closed gaps here with ✅ and link to resolving note)*

## Implementation Phase Gaps (Opened March 2026)

**GAP-07: Loss weight ratio not empirically validated**
The 0.7/0.3 Dice/BCE split is an informed estimate. Must be tuned during training.
- Status: 🔴 Open
- Action: Test 0.8/0.2 and 0.6/0.4 as alternatives during training phase

**GAP-08: MGT score achievability unknown for our architecture**
Target MGT > 0.80 set based on YOLOv8 benchmark (0.86). Not yet validated for EfficientNet-B0 + UNet++.
- Status: 🔴 Open
- Action: Validate post-training against CBIS-DDSM radiologist masks

**GAP-09: Input resolution tradeoff unresolved**
224x224 chosen for compute efficiency but may lose fine-grained mass boundary detail vs 512x512.
- Status: 🔴 Open
- Action: Run ablation after baseline model is trained
