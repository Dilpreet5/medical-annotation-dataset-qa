from pathlib import Path


def get_verified_images(folder_path: Path):

    if not folder_path.exists():
        return []

    images = []

    for file in folder_path.iterdir():
        if file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
            images.append(file)

    return images[:3]
