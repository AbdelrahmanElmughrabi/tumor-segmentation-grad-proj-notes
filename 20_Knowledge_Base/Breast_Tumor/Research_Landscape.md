---
type: research_summary
---

# Research Landscape

Parent: [[Breast_Tumor]]

> [!abstract] BLUF (Bottom Line Up Front)
> - **Primary Target:** 2D Mammography combined pipeline (Seg + Class + Explainability).
> - **The Gap:** No open-source project currently combines all three for mammography.
> - **North Star Repos:** [[caumente/multi_task_breast_cancer]] for architecture logic; [[monajemi-arman/breast_cancer_detection]] for mammo preprocessing.
> - **Tech Stack:** PyTorch + MONAI + `pytorch-grad-cam`.

---

So I spent some time going through a bunch of open source projects and deep research reports to understand what's actually out there for breast tumor detection, segmentation, and classification. The goal was simple — before we decide what to build, I wanted to know what already exists, what patterns keep showing up, and where the gaps are. Here's what I found.

---

## The 2D World

The 2D mammography space is the most active. Most projects I found focused on detection — meaning they tell you *where* a tumor is via a bounding box, not what it looks like at a pixel level. The tools used here are mostly YOLOv8, Faster R-CNN via Detectron2, and ResNet-based classifiers. A good example is monajemi-arman's project which chains YOLOv8 and Faster R-CNN together with a full DICOM conversion and preprocessing pipeline — it's probably the most complete detection-only pipeline I found. Another one from Kheiron Medical (mammo-net) uses ResNet on VinDr-Mammo, 20,000 images, straightforward classification setup.

The interesting thing is that when you look at segmentation specifically — meaning pixel-level tumor boundary delineation — the options get thinner. I found Bi-CBMSegNet which got 97.81% Dice on INbreast using a dual-module encoder-decoder with a balanced hybrid loss, but there's no standalone repo for it. There's also Ashayp31's project which is a clean U-Net segmentation implementation on mammography with good GPU training documentation, and Holliemin9090's Mask R-CNN project that does bounding box + mask simultaneously.

What stood out: nobody combined segmentation + classification + explainability in one clean pipeline for mammography. Detection exists. Segmentation exists. Classification exists. But not together, and not with Grad-CAM on top.

On the ultrasound side (still 2D), caumente's multi_task_breast_cancer is the closest thing I found to what we want to build — it does shared-backbone segmentation + classification using U-Net++ on the BUSI dataset. It even handles data curation properly by removing duplicates that caused data leakage in previous work. The architecture pattern is exactly what we'd want, just on ultrasound instead of mammography. There's also a DenseNet121 classification project on BUSI that's clean and has a Streamlit deployment, worth looking at for the classification head design.

---

## The 3D World

3D breast imaging splits across three distinct modalities and each one has a different ecosystem.

**MRI (DCE-MRI)** is the most mature. MAMA-MIA is the gold standard here — nnU-Net v2 trained on 1,506 expert-annotated cases across multiple cohorts, preprocessing standardized, pre-trained weights available, Dice 0.76 on full tumor. If we ever go 3D on MRI, this is the benchmark to beat and also the pipeline to understand. There's also BreastDCEDL which uses a Vision Transformer to predict chemotherapy response from 3 temporal MRI phases — interesting framing, different task. And BreastCancerDiagnosisMRI which does detection + Grad-CAM slice by slice on breast MRI, which is actually relevant to us because it shows Grad-CAM being applied to breast imaging in a deployed way.

**DBT (Digital Breast Tomosynthesis)** is 3D mammography essentially — multiple X-ray angles reconstructed into a volume. TomoLIBRA handles volumetric breast density estimation using a 3D CNN via GaNDLF framework, trained on a massive 1.63TB dataset. The dataset scale alone tells you this is not a weekend project. There's also priyak307's project that applies Detectron2 and YOLOv8 to DBT DICOM volumes for detection. DBT is the natural upgrade from 2D mammography if we ever go that route — same modality, more context.

**ABUS (Automated 3D Ultrasound)** has the TDSC-ABUS challenge codebase which uses 3D UNet++, Swin-UNETR, and STU-NET with weighted Dice + Focal loss. Solid for tumor boundary delineation in 3D ultrasound. Less relevant to our mammography focus but the nested skip connection architecture (UNet++) is worth knowing about.

One thing I noticed across all 3D projects — compute requirements are significant. MAMA-MIA uses multi-GPU, TomoLIBRA requires CUDA 11.8/12.2 with multi-GPU support. The only 3D approach that fits comfortably on a single 16GB GPU is a lightweight patch-based architecture with 128x128x128 patches.

---

## What the Field Is Missing

> [!important] The Research Gap
> After going through all of this, the gap is clear: **there is no open source project that puts segmentation + benign/malignant classification + Grad-CAM explainability into a single end-to-end pipeline specifically for 2D mammography.** Each piece exists somewhere — segmentation exists in Bi-CBMSegNet, classification exists in mammo-net, Grad-CAM has been applied to breast MRI in BreastCancerDiagnosisMRI — but nobody connected all three for mammography. That's the space we're working in.

Beyond our specific gap, I also noticed that most mammography projects skip explainability entirely. Detection models tell you where, classification models tell you what, but very few show you why in a way a clinician could actually use.

---

## What We Can Build and What's Actionable

Based on everything I found, a few things are clear. The multi-task U-Net pattern — shared encoder splitting into a segmentation decoder and a classification head — is the proven architecture for this kind of combined task. caumente proved it works for breast ultrasound with U-Net++. The architecture is transferable to mammography, the dataset is what changes.

For explainability, jacobgil's pytorch-grad-cam library hooks directly into PyTorch U-Net layers and is the standard tool. BreastCancerDiagnosisMRI shows the pattern applied to breast imaging specifically — adapting it to the segmentation branch (Seg-Grad-CAM) is the open implementation question.

The preprocessing side is less standardized for mammography than for MRI. CLAHE, histogram equalization, DICOM conversion, directional flipping — these steps appear across multiple projects but there's no consensus on the exact pipeline for a combined seg+class task. That's something we'll need to experiment with once the dataset is confirmed.

The dataset decision is still open. CBIS-DDSM, INbreast, and VinDr-Mammo are the realistic candidates. Each has different annotation quality and size. That choice will shape everything else downstream.

3D (DBT) stays in perspective as an upgrade path — but the 2D pipeline comes first.

---

*See detailed notes in each modality file. See open questions in [[Mammography_Gaps]]. All sources credited in [[Open_Sourced_Sources]].*
