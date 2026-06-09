import pandas as pd
import shutil
import os

# Load NIH bounding box CSV
df = pd.read_csv("BBox_List_2017.csv")

# Fix column names
df.columns = [
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

# Keep only expert-labeled diseases
cardiomegaly = df[df["label"] == "Cardiomegaly"]
infiltrate = df[df["label"] == "Infiltrate"]

# Take first 20 images each (for testing)
cardiomegaly = cardiomegaly.head(20)
infiltrate = infiltrate.head(20)

# Create folders
folders = {
    "cardiomegaly": "project_dataset/cardiomegaly_expert",
    "infiltrate": "project_dataset/infiltrate_expert"
}

for folder in folders.values():
    os.makedirs(folder, exist_ok=True)

# Search image folders
source_folders = [
    "images_001/images",
    "images_002/images"
]

def copy_images(dataframe, destination):

    for _, row in dataframe.iterrows():

        image_name = row["image"]
        found = False

        for folder in source_folders:

            source_path = os.path.join(folder, image_name)

            if os.path.exists(source_path):

                shutil.copy(source_path, destination)

                print(f"Copied: {image_name}")

                found = True
                break

        if not found:
            print(f"Not found: {image_name}")

# Copy files
copy_images(cardiomegaly, folders["cardiomegaly"])
copy_images(infiltrate, folders["infiltrate"])

print("\n✅ Done! Expert images copied.")
