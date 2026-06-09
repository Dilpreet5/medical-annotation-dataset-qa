import shutil
import os

# Where your extracted images are
source_folders = [
    "images_001/images",
    "images_002/images"
]

# Destination folders
destinations = {
    "healthy": "project_dataset/healthy",
    "cardiomegaly": "project_dataset/cardiomegaly",
    "infiltration": "project_dataset/infiltration"
}

# 30-image starter set
files = {
    "healthy": [
        "00000002_000.png",
        "00000005_000.png",
        "00000005_003.png",
        "00000005_004.png",
        "00000005_005.png",
        "00000006_000.png",
        "00000007_000.png",
        "00000008_001.png",
        "00000011_001.png",
        "00000011_002.png"
    ],

    "cardiomegaly": [
        "00000001_000.png",
        "00000008_000.png",
        "00000013_045.png",
        "00000044_002.png",
        "00000045_000.png",
        "00000069_000.png",
        "00000075_000.png",
        "00000075_001.png",
        "00000077_000.png",
        "00000096_000.png"
    ],

    "infiltration": [
        "00000005_006.png",
        "00000010_000.png",
        "00000011_007.png",
        "00000013_046.png",
        "00000021_001.png",
        "00000026_000.png",
        "00000043_000.png",
        "00000051_000.png",
        "00000054_000.png",
        "00000054_006.png"
    ]
}

# Create destination folders if missing
for folder in destinations.values():
    os.makedirs(folder, exist_ok=True)

# Copy files
for category, filenames in files.items():

    destination = destinations[category]

    for fname in filenames:
        copied = False

        for folder in source_folders:
            source_path = os.path.join(folder, fname)

            if os.path.exists(source_path):
                shutil.copy(source_path, destination)
                print(f"Copied {fname} → {category}")
                copied = True
                break

        if not copied:
            print(f"Not found: {fname}")

print("\n✅ Done! All images copied.")