import tensorflow as tf
from tensorflow.keras import layers, models # type: ignore
import matplotlib.pyplot as plt
import numpy  as np

def editArray(imagearray):
    imagearray = np.expand_dims(imagearray, axis=-1)
    imagearray = np.expand_dims(imagearray, axis=0)
    return imagearray

def predict(array, modelname):
    model = models.load_model(modelname)
    array = editArray(array)
    predictions = model.predict(array)
    predicted_class = np.argmax(predictions, axis=1)
    return predictions, predicted_class

if(__name__ == '__main__'):
    predict('C:\\Users\\пк\\Downloads\\array.json','my_model.keras')
