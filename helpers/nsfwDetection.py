import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
from tensorflow import keras
from helpers.preprocessImgs import prepare_img

#First things first check for nudity

#Loading the model
print("--------Loading the model---------")
model = keras.models.load_model('./model')

def nsfw_detection(img_path):
    """
    PARAMS::
    - img_path a path for the image that I'm gonna to work on
    Returns::
    - return a numpy array with 3 values representing our 3 classes
    0 for drugs, 1 for violence, 2 for natural
    """

    img = prepare_img(img_path)
    preds = model.predict(img)
    print(f"{preds} \n {preds.shape} here is our predictions")
    return preds
