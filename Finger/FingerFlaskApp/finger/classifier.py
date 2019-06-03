import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet import preprocess_input
from tensorflow.keras.models import Model, model_from_json


class Classifier:

    def __init__(self):
        reader = open('C:\\Users\\LG\\PycharmProjects\\Finger\\finger\\CNN_finger_model', 'r')
        CNN_finger_model = reader.read()
        reader.close()
        self.CNN_finger_model = model_from_json(CNN_finger_model)
        self.CNN_finger_model.load_weights("C:\\Users\\LG\\PycharmProjects\\Finger\\finger\\CNN_finger_weight.h5")

    def convert_image(self, image_src):
        img = image.load_img('C:\\Users\\LG\\PycharmProjects\\Finger\\finger' + image_src, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        return x

    def predict(self, image_src):
        converted = self.convert_image(image_src)
        result = self.CNN_finger_model.predict(converted).argmax()
        return result