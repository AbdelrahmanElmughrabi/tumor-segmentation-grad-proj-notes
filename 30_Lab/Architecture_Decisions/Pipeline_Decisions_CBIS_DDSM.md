---
tags:
  - status/verified
  - topic/architecture
date: 2026-03
---
# Architecture Decision Log
## Breast Mammography AI Pipeline — CBIS-DDSM

Project: Tumor Segmentation Using Deep Learning
Team: Dilara Sönmez (20COMP1015), Abdelrahman Elmughrabi (21SOFT1070)
Date: March 2026
Status: Decisions validated against CBIS-DDSM specific research (2019–2025)

---

## Decision 1 — Preprocessing Pipeline

**Decision:** MONAI transforms pipeline: DICOM load → morphological opening → Otsu + region-growing pectoral mask → CLAHE (8x8 tiles) → zero-pad to square → resize 224x224 → Z-score normalize.

**Reasoning:** CBIS-DDSM is digitized screen-film mammography — noisier and more artifact-heavy than modern FFDM datasets. Standard preprocessing is insufficient.

**Evidence:**
- CLAHE boosted EfficientNetV2 accuracy from 91.1% → 99.4% on CBIS-DDSM. Most significant single preprocessing gain documented.
- Pectoral muscle removal via Otsu + region-growing achieved 96% success rate on MLO views. Without it, models erroneously correlate bright pectoral regions with malignancy.
- MONAI transforms apply geometric operations to image and mask simultaneously — directly prevents the spatial misalignment pitfall documented in CBIS-DDSM implementations.

**Alternative considered:** Standard global histogram equalization.
**Why rejected:** Documented to over-amplify background noise in fatty regions, artificially simulating microcalcifications and destroying clinical fidelity.

**Risk:** Spatial misalignment if transforms are not applied jointly to image and mask. Mitigated by MONAI.

---

## Decision 2 — Segmentation Architecture

**Decision:** UNet++ with EfficientNet-B0 encoder pretrained on ImageNet.

**Reasoning:** Best efficiency/accuracy tradeoff on CBIS-DDSM. Nested skip connections handle spiculated mass margins that standard U-Net fails on.

**Evidence:**
- UNet++ reported Dice 0.929, IoU 0.871 on CBIS-DDSM mass segmentation with only 9M parameters.
- Standard U-Net capped at Dice 0.810–0.830 — insufficient for spiculated margins.
- Mask R-CNN achieves Dice 0.941 but exceeds single GPU deployment constraints and requires significantly more VRAM.
- EfficientNet-B0 encoder provides pretrained ImageNet feature initialization — reduces training time and data requirement.

**Alternative considered:** Mask R-CNN.
**Why rejected:** Dice gain of ~0.012 over UNet++ does not justify the computational cost increase. Not feasible on Kaggle T4 at reasonable batch sizes.

**Alternative considered:** Standard U-Net.
**Why rejected:** Dice 0.810–0.830 is too weak for spiculated mass boundary delineation. Semantic gap between encoder and decoder features not adequately bridged.

**Risk:** None critical. UNet++ is well-validated on CBIS-DDSM with public implementations available.

---

## Decision 3 — Classification Architecture

**Decision:** Shared EfficientNet-B0 encoder + CBAM (Convolutional Block Attention Module) + GAP → Dense(256) → Dropout(0.5) → Dense(1) → Sigmoid. Binary output: benign/malignant.

**Reasoning:** CBAM forces the network to attend to lesion-specific features and suppress fibroglandular background noise. Sharing the encoder with the segmentation branch enables mutual regularization between tasks.

**Evidence:**
- EfficientNet-B0 + CBAM reported accuracy >99.1%, AUC >0.996 on CBIS-DDSM.
- CBAM documented to suppress background noise and force spatial attention onto lesion features — critical for mammography where healthy tissue dominates.
- ASG-MammoNet (EfficientNet-B0 + dual CBAM, shared backbone) achieved 99.78% ± 0.09% accuracy, AUC >0.996, 14ms inference — closest validated reference to our pipeline.
- Shared encoder validated by MTL research: joint optimization improves segmentation recall +4.13% and classification accuracy +2.34% vs single-task baselines.

**Alternative considered:** Separate ResNet-50 classification backbone.
**Why rejected:** ResNet-50 AUC 0.858–0.95 on CBIS-DDSM — lower than EfficientNet. Separate backbone adds parameters and removes MTL mutual regularization benefit.

**Risk:** CBAM adds moderate complexity. Well-documented in literature and available in standard PyTorch implementations.

---

## Decision 4 — BI-RADS Label Mapping

**Decision:** BI-RADS 1, 2 → Benign. BI-RADS 4A/4B/4C, 5, 6 → Malignant. Exclude BI-RADS 3 from training and test sets entirely.

**Reasoning:** BI-RADS 3 ("Probably Benign") has no immediate biopsy confirmation in retrospective datasets. Including it introduces label ambiguity that degrades model decision boundaries.

**Evidence:**
- Explicitly documented in CBIS-DDSM literature: "models trained on datasets explicitly pruned of BI-RADS 3 demonstrate significantly sharper decision boundaries and higher AUCs."
- BI-RADS 3 clinical protocol recommends 6-month follow-up rather than immediate biopsy — meaning ground truth labels are unreliable for these cases.
- Consensus across rigorous CBIS-DDSM implementations: exclude BI-RADS 3.

**Alternative considered:** Include BI-RADS 3 as Benign.
**Why rejected:** Artificially blurs the hyperplane between benign and malignant classes. Documented to weaken generalizability.

**Risk:** Reduces available training samples. Acceptable tradeoff for label quality.

---

## Decision 5 — Multi-Task Loss Function

**Decision:** L_total = 0.7 × Dice Loss (segmentation) + 0.3 × Binary Cross-Entropy (classification).

**Reasoning:** Segmentation loss must dominate to force the shared encoder to learn spatially precise morphological features. These features then enrich the classification head.

**Evidence:**
- MTL-OCA and NMTNet both demonstrate seg-dominant loss weighting improves both tasks simultaneously on mammography benchmarks.
- General MTL principle validated: heavy segmentation weighting forces encoder to learn boundary-aware features that benefit classification.

**Flag:** The exact 0.7/0.3 split is an informed estimate — not a directly reported value from CBIS-DDSM literature. Must be treated as a starting point and tuned empirically during training. Test 0.8/0.2 and 0.6/0.4 as alternatives.

**Risk:** Loss weight imbalance is the primary tuning variable in MTL. Requires ablation study during training phase.

---

## Decision 6 — Explainability Method

**Decision:** Grad-CAM++ via jacobgil/pytorch-grad-cam hooked to the final convolutional layer of the shared EfficientNet-B0 encoder. Validate heatmaps using MGT score against CBIS-DDSM radiologist masks. Target MGT > 0.80.

**Reasoning:** Grad-CAM++ is the gold standard for spatial explainability in mammography. Quantitative validation against radiologist masks is now mandatory in rigorous implementations — purely visual inspection is no longer accepted.

**Evidence:**
- HiResCAM achieved MGT 0.4908 on CBIS-DDSM. YOLOv8 pipeline achieved MGT 0.86.
- ASG-MammoNet DIP score 0.99 ± 0.0047 — near-perfect spatial alignment with lesion centroid.
- Grad-CAM generation overhead: 0.29s per image including IO. Negligible for desktop app.
- CBAM attention modules documented to prevent heatmaps from highlighting pectoral muscle or tape marks — directly beneficial for CBIS-DDSM artifact issues.

**Alternative considered:** SHAP, LIME, Score-CAM.
**Why rejected:** Comparative studies on mammography show all three produce dispersed, clinically inconsistent maps compared to Grad-CAM. Grad-CAM consistently isolates lesion-specific areas with superior spatial precision.

**Risk:** MGT target of 0.80 is ambitious — YOLOv8 achieved 0.86 but with a different architecture. Validate against CBIS-DDSM masks post-training.

---

## Decision 7 — Framework and Training Configuration

**Decision:** PyTorch + MONAI. Patient-level 80/20 train/test split stratified by malignancy ratio. Batch size 16 at 224x224. Augmentation: rotation up to 90° + horizontal flip only.

**Reasoning:** PyTorch + MONAI is the dominant stack from 2022 onward. Patient-level split is mandatory to prevent data leakage. Conservative augmentation preserves CLAHE-processed intensity distributions.

**Evidence:**
- PyTorch + MONAI documented as the standard framework for CBIS-DDSM pipelines from 2022–2025. TensorFlow/Keras largely abandoned in recent literature.
- Image-level split explicitly called out as the most severe methodological error in CBIS-DDSM implementations — invalidates published results by causing data leakage between CC and MLO views of the same patient.
- GTX 1050Ti (4GB) and RTX 2060 (6GB) documented as sufficient hardware. Kaggle T4 (16GB) is very comfortable at batch 16, 224x224.
- Rotation + horizontal flip documented as highest individual Dice score gains. Extreme shearing documented to distort mass morphology detrimentally.

**Alternative considered:** Image-level split for simplicity.
**Why rejected:** Creates data leakage — CC and MLO views of same patient split across train and test sets. Model memorizes patient anatomy rather than learning tumor features.

**Risk:** Patient-level split reduces effective training samples. Stratified sampling by malignancy ratio mitigates statistical impact.

---

## Open Items (Require Empirical Validation)
- Loss weight ratio (0.7/0.3) — test 0.8/0.2 and 0.6/0.4 during training
- MGT score achievability with our architecture — validate post-training against CBIS-DDSM masks
- Input resolution tradeoff — 224x224 vs 512x512 for mass boundary precision
