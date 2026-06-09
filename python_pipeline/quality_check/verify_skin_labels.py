import os
import random
from PIL import Image, ImageDraw

# ---------------------
# Folders
# ---------------------

image_folder = "final_images/skin_images"
label_folder = "annotation/yolo_format/skin"
output_folder = "verified_skin"

os.makedirs(output_folder, exist_ok=True)

# Class names
classes = {
    0: "skin_lesion"
}

# Get images
image_files = [
    f for f in os.listdir(image_folder)
    if f.endswith(".jpg")
]

# Check ALL images
for image_name in image_files:

    image_path = os.path.join(
        image_folder,
        image_name
    )

    label_path = os.path.join(
        label_folder,
        image_name.replace(".jpg", ".txt")
    )

    if not os.path.exists(label_path):
        continue

    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    width, height = img.size

    with open(label_path, "r") as f:

        lines = f.readlines()

        for line in lines:

            parts = line.split()

            if len(parts) != 5:
                continue

            class_id = int(parts[0])

            x_center = float(parts[1])
            y_center = float(parts[2])
            box_width = float(parts[3])
            box_height = float(parts[4])

            # YOLO → pixels
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

            # Draw box
            draw.rectangle(
                [x1, y1, x2, y2],
                outline="red",
                width=4
            )

            # Draw label
            draw.text(
                (x1, y1 - 20),
                classes.get(
                    class_id,
                    "Unknown"
                ),
                fill="red"
            )

    # Save image
    save_path = os.path.join(
        output_folder,
        image_name
    )

    img.save(save_path)

    print(f"Done: {image_name}")

print(
    "\n✅ Skin verification complete!"
)