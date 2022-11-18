import os
from PIL import Image


def load_plant_village():
    current_path = os.getcwd()
    plant_village_path = os.path.join(current_path, 'PlantVillage')

    images = {}
    for directory in os.listdir(plant_village_path):
        images[directory] = []
        disease_directory = os.path.join(plant_village_path, directory)
        for _, file in enumerate(os.listdir(disease_directory)):
            image_path = os.path.join(disease_directory, file)
            with Image.open(image_path) as img:
                images[directory] += [img.copy()]

    return images
