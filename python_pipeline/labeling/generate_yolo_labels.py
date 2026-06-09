
import pandas as pd
import os
import shutil
from PIL import Image

bbox_df = pd.read_csv("BBox_List_2017.csv")
data_df = pd.read_csv("Data_Entry_2017.csv")

# Fix BBox column names
bbox_df.columns = [
    "image",
    "label",
    "x",
    "y",
    "w",
    "h",
    "extra1",
    "extra2",
    "extra3"
]

# -------------------------
# Classes
# -------------------------

wanted_labels = {
    "Cardiomegaly": 0,
    "Effusion": 1,
    "Pneumonia": 2,
    "Atelectasis": 3
}

HEALTHY_CLASS_ID = 4

max_per_class = 60
max_healthy = 60

# -------------------------
# Downloaded image folders
# -------------------------

source_folders = [
    "images_001/images",
    "images_002/images",
    "images_003/images",
    "images_004/images",
    "images_005/images",
    "images_006/images"
]

# -------------------------
# Output folders
# -------------------------

image_output = "project_dataset/images"
label_output = "project_dataset/labels"

os.makedirs(image_output, exist_ok=True)
os.makedirs(label_output, exist_ok=True)

# -------------------------
# Helper function
# -------------------------

def find_image(image_name):

    for folder in source_folders:

        path = os.path.join(folder, image_name)

        if os.path.exists(path):
            return path

    return None


# -------------------------
# Track counts
# -------------------------

class_counts = {
    "Cardiomegaly": 0,
    "Effusion": 0,
    "Pneumonia": 0,
    "Atelectasis": 0,
    "Healthy": 0
}

# -------------------------
# Process disease images
# -------------------------

for _, row in bbox_df.iterrows():

    label_name = row["label"]

    if label_name not in wanted_labels:
        continue

    if class_counts[label_name] >= max_per_class:
        continue

    image_name = row["image"]

    image_path = find_image(image_name)

    if not image_path:
        continue

    img = Image.open(image_path)
    img_width, img_height = img.size

    x = float(row["x"])
    y = float(row["y"])
    w = float(row["w"])
    h = float(row["h"])

    # Convert to YOLO format
    center_x = (x + w / 2) / img_width
    center_y = (y + h / 2) / img_height
    width = w / img_width
    height = h / img_height

    class_id = wanted_labels[label_name]

    # Copy image
    shutil.copy(image_path, image_output)

    # Save YOLO label
    txt_path = os.path.join(
        label_output,
        image_name.replace(".png", ".txt")
    )

    with open(txt_path, "w") as f:
        f.write(
            f"{class_id} "
            f"{center_x:.6f} "
            f"{center_y:.6f} "
            f"{width:.6f} "
            f"{height:.6f}"
        )

    class_counts[label_name] += 1

    print(f"Done: {image_name} → {label_name}")

# -------------------------
# Add Healthy images
# -------------------------

healthy_df = data_df[
    data_df["Finding Labels"] == "No Finding"
]

healthy_added = 0

for _, row in healthy_df.iterrows():

    if healthy_added >= max_healthy:
        break

    image_name = row["Image Index"]

    image_path = find_image(image_name)

    if not image_path:
        continue

    shutil.copy(image_path, image_output)

    # Empty YOLO txt file for healthy
    txt_path = os.path.join(
        label_output,
        image_name.replace(".png", ".txt")
    )

    open(txt_path, "w").close()

    healthy_added += 1
    class_counts["Healthy"] += 1

    print(f"Healthy: {image_name}")

# -------------------------
# Final summary
# -------------------------

print("\n✅ Dataset generated!")
print(class_counts)
print(
    "\nTotal images:",
    sum(class_counts.values())
)

