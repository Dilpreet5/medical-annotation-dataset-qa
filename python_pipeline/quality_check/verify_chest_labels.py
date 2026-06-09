import os
import random
from PIL import Image, ImageDraw

# Paths
image_folder = "project_dataset/images"
label_folder = "project_dataset/labels"
output_folder = "project_dataset/verified"

os.makedirs(output_folder, exist_ok=True)

# Class names
classes = {
    0: "Cardiomegaly",
    1: "Effusion",
    2: "Pneumonia",
    3: "Atelectasis"
}

# Get random images
image_files = [
    f for f in os.listdir(image_folder)
    if f.endswith(".png")
]

sample_images = image_files

for image_name in sample_images:

    image_path = os.path.join(
        image_folder,
        image_name
    )

    label_path = os.path.join(
        label_folder,
        image_name.replace(".png", ".txt")
    )

    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    width, height = img.size

    # Read label
    if os.path.exists(label_path):

        with open(label_path, "r") as f:

            lines = f.readlines()

            for line in lines:

                if line.strip() == "":
                    continue

                parts = line.split()

                class_id = int(parts[0])

                x_center = float(parts[1])
                y_center = float(parts[2])
                box_width = float(parts[3])
                box_height = float(parts[4])

                # Convert YOLO -> pixel coords
                x1 = (
                    x_center - box_width / 2
                ) * width

                y1 = (
                    y_center - box_height / 2
                ) * height

                x2 = (
                    x_center + box_width / 2
                ) * width

                y2 = (
                    y_center + box_height / 2
                ) * height

                # Draw rectangle
                draw.rectangle(
                    [x1, y1, x2, y2],
                    outline="red",
                    width=4
                )

                draw.text(
                    (x1, y1 - 20),
                    classes.get(
                        class_id,
                        "Unknown"
                    ),
                    fill="red"
                )

    # Save checked image
    save_path = os.path.join(
        output_folder,
        image_name
    )

    img.save(save_path)

    print(f"Checked: {image_name}")

print("\n✅ Visual check images created!")