from pathlib import Path
from utils.constants import DATASET_PATH


# chetogary
def get_dataset_stats():

    stats = {}

    for folder in DATASET_PATH.iterdir():

        if folder.is_dir():

            image_count = 0

            for file in folder.iterdir():

                if file.suffix.lower() in [".jpg", ".jpeg", ".png"]:

                    image_count += 1
                    

            stats[folder.name] = image_count

    
    return stats


if __name__ == "__main__":
    stats = get_dataset_stats()
    print(stats)


# number of images 
def total_image_count():

    image = get_dataset_stats()

    total = sum(image.values())

    return total  



# number of classes

def total_classes():

    classes_count = 0

    for item in DATASET_PATH.iterdir():

        if item.is_dir():

            classes_count += 1

    return classes_count




        

            


