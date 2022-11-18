from utils import load_plant_village
from tensorflow.image import random_crop
from tensorflow.image import random_contrast
from tensorflow.image import random_brightness
from tensorflow.image import random_flip_left_right
from tensorflow.image import random_hue
from tensorflow.image import random_jpeg_quality
from tensorflow.image import random_saturation
from tensorflow.keras.preprocessing.image import random_rotation
from PIL import Image
import numpy as np


def random_augmentation(img):
    img = random_rotation(img, 20, row_axis=0, col_axis=1, channel_axis=2, fill_mode='reflect')
    img = random_contrast(img, 0.8, 1.2)
    img = random_brightness(img, 0.08)
    img = random_hue(img, 0.025)
    img = random_saturation(img, 0.85, 1.15)
    img = random_jpeg_quality(img, 75, 95)
    img = random_flip_left_right(img)
    return random_crop(img, img).numpy()


def get_augmented_image(img):
    return Image.fromarray(np.array(img)).resize((224, 224))


if __name__ == '__main__':
    images = load_plant_village()
    img = random_augmentation(images['Apple___Apple_scab'][0])
    get_augmented_image(img).show()
