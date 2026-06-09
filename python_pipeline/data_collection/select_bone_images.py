import os
import random
import shutil

# ===== SETTINGS =====

SOURCE_FOLDER = "/home/dilpreet/Downloads/medical_project/bone _data/bone_images/Human Bone Fracture C17 Dataset"

DEST_FOLDER = "/home/dilpreet/Downloads/Medical-Annotation-Project/dataset/bone"

NUM_IMAGES = 100

# ====================

os.makedirs(DEST_FOLDER, exist_ok=True)

all_images = []

# collect all images from subfolders
for root, dirs, files in os.walk(SOURCE_FOLDER):

    for file in files:

        if file.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):

            full_path = os.path.join(root, file)

            all_images.append(full_path)

print(f"Found {len(all_images)} total images")

# random selection
selected_images = random.sample(
    all_images,
    min(NUM_IMAGES, len(all_images))
)

# copy files
for i, image_path in enumerate(selected_images, start=1):

    ext = os.path.splitext(image_path)[1]

    new_name = f"bone_{i:03d}{ext}"

    destination_path = os.path.join(
        DEST_FOLDER,
        new_name
    )

    shutil.copy(image_path, destination_path)

print(f"{len(selected_images)} bone images copied!")
print("Done!")