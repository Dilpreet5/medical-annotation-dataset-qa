import os
import shutil
import random

# ===== SETTINGS =====
NUM_CHEST_SAMPLES = 5
NUM_SKIN_SAMPLES = 5
BASE_DIR = os.getcwd()
PATHS = {
    "chest": {
        "raw": os.path.join(BASE_DIR, "dataset", "chest"),
        "labels": os.path.join(BASE_DIR, "annotations", "chest"),
        "verified": os.path.join(BASE_DIR, "verified_annotations", "chest")
    },
    "skin": {
        "raw": os.path.join(BASE_DIR, "dataset", "skin"),
        "labels": os.path.join(BASE_DIR, "annotations", "skin"),
        "verified": os.path.join(BASE_DIR, "verified_annotations", "skin")
    }
}

OUTPUT_DIR = os.path.join(BASE_DIR, "sample_dataset")


def create_samples(dataset_name, sample_count):
    raw_dir = PATHS[dataset_name]["raw"]
    label_dir = PATHS[dataset_name]["labels"]
    verified_dir = PATHS[dataset_name]["verified"]

    output_dataset_dir = os.path.join(OUTPUT_DIR, dataset_name)

    os.makedirs(output_dataset_dir, exist_ok=True)

    image_files = [
        f for f in os.listdir(raw_dir)
        if f.endswith((".png", ".jpg", ".jpeg"))
    ]

    random.shuffle(image_files)

    selected_images = image_files[:sample_count]

    for idx, image_name in enumerate(selected_images, start=1):

        image_base = os.path.splitext(image_name)[0]

        sample_folder = os.path.join(
            output_dataset_dir,
            f"sample_{idx:02d}"
        )

        os.makedirs(sample_folder, exist_ok=True)

        raw_image_path = os.path.join(raw_dir, image_name)
        label_path = os.path.join(label_dir, image_base + ".txt")
        verified_image_name = image_base + "_boxed.png"

        verified_image_path = os.path.join(
        verified_dir,
        verified_image_name
)

        # Copy raw image
        if os.path.exists(raw_image_path):
            shutil.copy(raw_image_path, sample_folder)

        # Copy txt label
        if os.path.exists(label_path):
            shutil.copy(label_path, sample_folder)

        # Copy boxed image
        if os.path.exists(verified_image_path):
            shutil.copy(verified_image_path, sample_folder)

    print(f"{dataset_name.upper()} samples created!")


# Create chest + skin samples
create_samples("chest", NUM_CHEST_SAMPLES)
create_samples("skin", NUM_SKIN_SAMPLES)

print("Sample dataset created successfully!")