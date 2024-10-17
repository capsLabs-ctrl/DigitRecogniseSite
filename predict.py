import tensorflow as tf
from tensorflow.keras import layers, models # type: ignore
import matplotlib.pyplot as plt
import json
import numpy  as np

def editArray(imagearray):
    imagearray = np.expand_dims(imagearray, axis=-1)
    imagearray = np.expand_dims(imagearray, axis=0)
    return imagearray

def predict(filepath, modelname):
    model = models.load_model(modelname)
    with open(filepath, 'r') as file:
        pixel_matrix = json.load(file)
    pixel_matrix = np.expand_dims(pixel_matrix, axis=-1)
    pixel_matrix = np.expand_dims(pixel_matrix, axis=0)
    predictions = model.predict(pixel_matrix)
    predicted_class = np.argmax(predictions, axis=1)
    return predictions, predicted_class

if(__name__ == '__main__'):
    predict('C:\\Users\\пк\\Downloads\\array.json','my_model.keras')
