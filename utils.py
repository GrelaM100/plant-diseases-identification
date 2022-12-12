import os
from PIL import Image

CLASS_TO_ID = {'Apple___Apple_scab': 0,
               'Apple___Black_rot': 1,
               'Apple___Cedar_apple_rust': 2,
               'Apple___healthy': 3,
               'Background_without_leaves': 4,
               'Blueberry___healthy': 5,
               'Cherry___healthy': 6,
               'Cherry___Powdery_mildew': 7,
               'Corn___Cercospora_leaf_spot Gray_leaf_spot': 8,
               'Corn___Common_rust': 9,
               'Corn___healthy': 10,
               'Corn___Northern_Leaf_Blight': 11,
               'Grape___Black_rot': 12,
               'Grape___Esca_(Black_Measles)': 13,
               'Grape___healthy': 14,
               'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': 15,
               'Orange___Haunglongbing_(Citrus_greening)': 16,
               'Peach___Bacterial_spot': 17,
               'Peach___healthy': 18,
               'Pepper,_bell___Bacterial_spot': 19,
               'Pepper,_bell___healthy': 20,
               'Potato___Early_blight': 21,
               'Potato___healthy': 22,
               'Potato___Late_blight': 23,
               'Raspberry___healthy': 24,
               'Soybean___healthy': 25,
               'Squash___Powdery_mildew': 26,
               'Strawberry___healthy': 27,
               'Strawberry___Leaf_scorch': 28,
               'Tomato___Bacterial_spot': 29,
               'Tomato___Early_blight': 30,
               'Tomato___healthy': 31,
               'Tomato___Late_blight': 32,
               'Tomato___Leaf_Mold': 33,
               'Tomato___Septoria_leaf_spot': 34,
               'Tomato___Spider_mites Two-spotted_spider_mite': 35,
               'Tomato___Target_Spot': 36,
               'Tomato___Tomato_mosaic_virus': 37,
               'Tomato___Tomato_Yellow_Leaf_Curl_Virus': 38}


def load_plant_village():
    current_path = os.getcwd()
    plant_village_path = os.path.join(current_path, 'datasets/original/PlantVillage')

    images = {}
    for directory in os.listdir(plant_village_path):
        images[directory] = []
        disease_directory = os.path.join(plant_village_path, directory)
        for _, file in enumerate(os.listdir(disease_directory)):
            image_path = os.path.join(disease_directory, file)
            with Image.open(image_path) as img:
                images[directory] += [img.copy()]

    return images


def load_plant_village_dataset(directory):
    dataset = []
    for d in os.listdir(directory):
        disease_directory = os.path.join(directory, d)
        for _, file in enumerate(os.listdir(disease_directory)):
            image_path = os.path.join(disease_directory, file)
            with Image.open(image_path) as img:
                single_record = {'image': img.copy(), 'label': CLASS_TO_ID[d]}
                dataset.append(single_record)

    return dataset


def load_augmented_plant_village(dataset='train'):
    current_path = os.getcwd()
    if dataset == 'train':
        dataset_dir = os.path.join(current_path, 'datasets/augmented/PlantVillage/train')
    elif dataset == 'test':
        dataset_dir = os.path.join(current_path, 'datasets/augmented/PlantVillage/test')
    else:
        dataset_dir = os.path.join(current_path, 'datasets/augmented/PlantVillage/val')

    dataset = load_plant_village_dataset(dataset_dir)
    return dataset
