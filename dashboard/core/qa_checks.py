from pathlib import Path
from utils.constants import ANNO_PATH
from PIL import Image
from utils.constants import DATASET_PATH

# def read_text_files():  [--- IGNORE ---]

#     bad_files = []

#     for file in ANNO_PATH.glob("**/*.txt"):

#         content = file.read_text().strip()

#         if content == "":
#             bad_files.append(file.name)

#     return bad_files



#dataset validation logic

def validate_dataset():
    corrupted_files = []

    for file in DATASET_PATH.rglob("*"):
        # only check image files
        if file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
            try:
                with Image.open(file) as img:
                    img.verify()
            except (IOError, SyntaxError):
                corrupted_files.append(file.name)

    return corrupted_files



#Missing Label Detection

def detect_missing_labels():
    missing_labels = []

    for image_file in DATASET_PATH.rglob("*"):

        if image_file.suffix.lower() in [".jpg", ".jpeg", ".png"]:

            class_folder = image_file.parent.name

            # Bone dataset has no annotation files by design
            if class_folder == "bone":
                continue

            label_file = (
                ANNO_PATH
                / class_folder
                / image_file.with_suffix(".txt").name
            )

            if not label_file.exists():
                missing_labels.append(image_file.name)

    return missing_labels