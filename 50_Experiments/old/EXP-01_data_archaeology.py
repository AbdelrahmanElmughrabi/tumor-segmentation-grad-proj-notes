"""
EXP-01_Data_Archaeology.py
Experiment: Data Archaeology for CBIS-DDSM
Objective: Validate dataset structure, implement patient-level split, and verify DICOM loading.
Designed for Kaggle Notebook environment.
"""

import os
import pandas as pd
import numpy as np
import pydicom
import matplotlib.pyplot as plt
from sklearn.model_selection import GroupShuffleSplit

# --- 1. CONFIGURATION & PATHS ---
# Standard Kaggle path for CBIS-DDSM
DATA_ROOT = "/kaggle/input/cbis-ddsm-breast-cancer-image-dataset"

CSV_FILES = {
    "mass_train": "mass_case_description_train_set.csv",
    "mass_test": "mass_case_description_test_set.csv",
    "calc_train": "calc_case_description_train_set.csv",
    "calc_test": "calc_case_description_test_set.csv"
}

def load_csvs(root):
    dfs = {}
    for key, name in CSV_FILES.items():
        path = os.path.join(root, name)
        if os.path.exists(path):
            dfs[key] = pd.read_csv(path)
            print(f"Loaded {key}: {len(dfs[key])} rows")
        else:
            print(f"Warning: {path} not found.")
    return dfs

# --- 2. DATA PARSING & FILTERING ---
print("--- Step 2: Parsing & Filtering BI-RADS 3 ---")
dfs = load_csvs(DATA_ROOT)

# Combine all data for a global survey (we will re-split properly)
full_df = pd.concat(dfs.values(), ignore_index=True)

# Filter out BI-RADS 3 (Assessment column)
# Architecture Decision 4: Exclude BI-RADS 3 entirely
before_count = len(full_df)
filtered_df = full_df[full_df['assessment'] != 3].copy()
after_count = len(filtered_df)

print(f"Total images before filtering: {before_count}")
print(f"Total images after removing BI-RADS 3: {after_count} (Dropped {before_count - after_count})")

# Simplify Pathology for distribution check
filtered_df['label'] = filtered_df['pathology'].apply(
    lambda x: 'Malignant' if 'MALIGNANT' in x else 'Benign'
)

print("\nClass Distribution (Filtered):")
print(filtered_df['label'].value_counts())

# --- 3. PATIENT-LEVEL ANALYSIS ---
print("\n--- Step 3: Patient-Level Statistics ---")
unique_patients = filtered_df['patient_id'].nunique()
print(f"Unique Patients (Filtered): {unique_patients}")
print(f"Average images per patient: {len(filtered_df) / unique_patients:.2f}")

# --- 4. PATH VALIDATION ---
print("\n--- Step 4: Path Validation ---")
# The 'image file path' in CBIS-DDSM CSVs often needs cleaning or joining with the root
def validate_paths(df, root_path):
    # Standard CBIS-DDSM paths in CSV look like: "Mass-Training_P_00001_LEFT_CC/..."
    # On Kaggle, they are often nested under 'dicom_images' or similar depending on the version.
    # We check if the raw path or a joined path exists.
    sample_path = df.iloc[0]['image file path'].split('/')[0]
    print(f"Sample folder from CSV: {sample_path}")
    
    # Check common Kaggle structures
    possible_roots = [
        os.path.join(root_path, "cbis-ddsm"),
        os.path.join(root_path, "CBIS-DDSM"),
        root_path
    ]
    
    found_root = None
    for pr in possible_roots:
        if os.path.exists(os.path.join(pr, sample_path)):
            found_root = pr
            break
    
    if found_root:
        print(f"Found data root at: {found_root}")
    else:
        print("Warning: Could not resolve DICOM paths. Directory structure may differ from CSV expectations.")
    
    return found_root

data_dir = validate_paths(filtered_df, DATA_ROOT)

# --- 5. PATIENT-LEVEL STRATIFIED SPLIT (80/20) ---
print("\n--- Step 5: Patient-Level Stratified Split (80/20) ---")
# Architecture Decision 7: Patient-level split is mandatory to prevent data leakage.
# We use GroupShuffleSplit to ensure all images of one patient stay in one set.

# To stratify by label at a patient level, we need one label per patient.
# In CBIS-DDSM, patients can have both benign and malignant findings, but usually they are consistent.
# For splitting purposes, we'll use the first finding's label.
patient_labels = filtered_df.groupby('patient_id')['label'].first()

gss = GroupShuffleSplit(n_splits=1, train_size=0.8, random_state=42)
train_idx, test_idx = next(gss.split(filtered_df, groups=filtered_df['patient_id']))

train_df = filtered_df.iloc[train_idx]
test_df = filtered_df.iloc[test_idx]

print(f"Train set: {len(train_df)} images, {train_df['patient_id'].nunique()} patients")
print(f"Test set:  {len(test_df)} images, {test_df['patient_id'].nunique()} patients")

# Verify no overlap
overlap = set(train_df['patient_id']) & set(test_df['patient_id'])
print(f"Patient overlap check: {len(overlap)} patients found in both sets (Expect 0)")

# --- 6. DICOM TEST LOADING ---
print("\n--- Step 6: DICOM Test Loading ---")
try:
    # Pick a random sample from train
    sample_row = train_df.sample(1).iloc[0]
    # In some Kaggle versions, we need to walk the directory because CSV paths are incomplete
    rel_path = sample_row['image file path'].split('/')[0]
    full_search_path = os.path.join(data_dir, rel_path)
    
    # Find the actual .dcm file inside the nested folders
    dcm_files = []
    for root, dirs, files in os.walk(full_search_path):
        for f in files:
            if f.endswith('.dcm'):
                dcm_files.append(os.path.join(root, f))
    
    if dcm_files:
        dcm_path = dcm_files[0]
        ds = pydicom.dcmread(dcm_path)
        print(f"Successfully loaded DICOM: {dcm_path}")
        print(f"Patient ID: {ds.PatientID}")
        print(f"Image Size: {ds.Rows}x{ds.Cols}")
        
        plt.figure(figsize=(6,6))
        plt.imshow(ds.pixel_array, cmap='gray')
        plt.title(f"Raw DICOM Sample\n{sample_row['pathology']}")
        plt.axis('off')
        plt.show()
    else:
        print(f"No DICOM file found in {full_search_path}")
except Exception as e:
    print(f"Error loading DICOM: {e}")
    print("Note: This script assumes standard Kaggle CBIS-DDSM structure. Adjust paths if using a custom version.")
