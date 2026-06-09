# Medical Annotation Dataset QA & Validation Tool

A healthcare-focused data annotation and quality validation project built using medical imaging datasets.

This project focuses on collecting, organizing, labeling, and validating medical image datasets across multiple imaging domains. The goal was to create a structured medical annotation workflow using Python automation, YOLO annotation format, and visual verification methods.

The project currently includes chest X-rays, skin lesion images, and bone fracture X-rays.

---

## Project Goal

The goal of this project was to:

* Collect real medical imaging datasets
* Generate annotation labels in YOLO format
* Verify annotation quality visually
* Organize data for future quality analysis and dashboard development
* Build a structured medical annotation pipeline that can later be used for dataset QA

Rather than training a medical AI model, this project focuses on the **data annotation and validation side** of healthcare AI workflows.

---

## Dataset Categories

### 1. Chest X-ray Dataset

Dataset source: NIH Chest X-ray Dataset

Medical categories used:

* Healthy
* Cardiomegaly
* Effusion
* Pneumonia
* Atelectasis

Collected:

* ~280 chest X-ray images

Labeling approach:

* Used Python automation for dataset preparation
* Generated YOLO `.txt` labels
* Used metadata and bounding box information
* Performed visual verification for label checking

---

### 2. Skin Lesion Dataset

Dataset source: ISIC Skin Lesion Dataset

Collected:

* ~50 skin lesion images

Labeling approach:

* Generated YOLO annotation labels
* Performed visual checking of lesion areas
* Organized annotations for dataset consistency

---

### 3. Bone Fracture Dataset

Dataset source: Human Bone Fracture C17 Dataset

Collected:

* ~100 bone fracture X-ray images

Current status:

* Raw dataset organized
* Data prepared for future annotation work

---

## Project Structure

```text
Medical-Annotation-Project/

├── annotations/
│   ├── bone/
│   ├── chest/
│   └── skin/
│
├── dataset/
│   ├── bone/
│   ├── chest/
│   └── skin/
│
├── python_pipeline/
│   ├── data_collection/
│   ├── labeling/
│   └── quality_check/
│
├── sample_dataset/
│
├── screenshots/
│
├── verified_annotations/
│
└── README.md
```

---

## Technologies Used

* Python
* Pandas
* OpenCV
* PIL
* Matplotlib
* YOLO annotation format

---

## Annotation Workflow

The workflow followed in this project:

1. Medical datasets were collected from public healthcare sources.
2. Images were organized into domain-specific folders.
3. YOLO annotation labels were generated using Python scripts.
4. Labels were visually verified using bounding box outputs.
5. Sample datasets were created for easier inspection and portfolio presentation.

---

## Sample Dataset

A small sample dataset is included inside:

```text
sample_dataset/
```

This folder contains example medical images, annotation files, and verification outputs used for quick inspection without uploading the full dataset.

---

## Screenshots

Project screenshots include:

* Dataset collection
* YOLO annotation generation
* Label verification process
* Project folder structure

---

## Future Work

Planned improvements for the next version:

* Dataset quality analysis script
* Class distribution statistics
* Annotation imbalance detection
* Streamlit dashboard for dataset validation
* Downloadable QA reports

---

## Notes

This project is intended for educational and portfolio purposes. It focuses on medical dataset preparation and annotation workflow rather than medical diagnosis.
