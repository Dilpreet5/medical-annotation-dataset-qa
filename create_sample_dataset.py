import os
import shutil
import random

BASE_DIR = os.getcwd()

NUM_CHEST = 5
NUM_SKIN = 5
NUM_BONE = 5


DATASETS = {
    "chest": {
        "raw": "dataset/chest",
        "labels": "annotations/chest",
        "verified": "verified_annotations/chest",
        "count": NUM_CHEST,
        "needs_labels": True
    },

    "skin": {
        "raw": "dataset/skin",
        "labels": "annotations/skin",
        "verified": "verified_annotations/skin",
        "count": NUM_SKIN,
        "needs_labels": True
    },

    "bone": {
        "raw": "dataset/bone",
        "count": NUM_BONE,
        "needs_labels": False
    }
}


def recreate_folder(path):
    if os.path.exists(path):
        shutil.rmtree(path)

    os.makedirs(path)


def create_samples(dataset_name, config):

    raw_dir = os.path.join(
        BASE_DIR,
        config["raw"]
    )

    output_dir = os.path.join(
        BASE_DIR,
        "sample_dataset",
        dataset_name
    )

    os.makedirs(output_dir, exist_ok=True)

    image_files = [
        f for f in os.listdir(raw_dir)
        if f.lower().endswith(
            (".png", ".jpg", ".jpeg", ".webp")
        )
    ]

    random.shuffle(image_files)

    selected_images = image_files[
        :config["count"]
    ]

    for idx, image_name in enumerate(
        selected_images,
        start=1
    ):

        sample_folder = os.path.join(
            output_dir,
            f"sample_{idx:02d}"
        )

        os.makedirs(sample_folder)

        image_base = os.path.splitext(
            image_name
        )[0]

        raw_image_path = os.path.join(
            raw_dir,
            image_name
        )

        shutil.copy(
            raw_image_path,
            sample_folder
        )

        if config["needs_labels"]:

            label_path = os.path.join(
                BASE_DIR,
                config["labels"],
                image_base + ".txt"
            )

            if os.path.exists(label_path):

                shutil.copy(
                    label_path,
                    sample_folder
                )

            verified_path = os.path.join(
                BASE_DIR,
                config["verified"],
                image_base + "_boxed.png"
            )

            if os.path.exists(
                verified_path
            ):

                shutil.copy(
                    verified_path,
                    sample_folder
                )

    print(
        f"{dataset_name.upper()} samples created!"
    )


sample_dataset_dir = os.path.join(
    BASE_DIR,
    "sample_dataset"
)

recreate_folder(
    sample_dataset_dir
)

for dataset_name, config in DATASETS.items():

    create_samples(
        dataset_name,
        config
    )

print(
    "\nSample dataset created successfully!"
)