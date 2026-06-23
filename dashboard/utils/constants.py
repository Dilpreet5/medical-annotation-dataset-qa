from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

DATASET_PATH = BASE_DIR / "dataset"
ANNO_PATH = BASE_DIR / "annotations"
VERIFIED_PATH = BASE_DIR / "verified_annotations"
CHEST_XRAY_PATH = VERIFIED_PATH / "chest"
BONE_PATH = VERIFIED_PATH / "bone"
SKIN_PATH = VERIFIED_PATH / "skin"

