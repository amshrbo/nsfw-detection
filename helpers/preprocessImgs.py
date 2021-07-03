from PIL import Image
import numpy as np
from tensorflow.keras.applications.mobilenet import preprocess_input
import os

img_sze = (224, 224)

def prepare_img(img_path):
  """
  params::
  - img_path: the image path that I'm gonna preprocess it to make it suitable for predictions
  returns:
  - Returns a numpy image 
  """
  try:
    img = Image.open(img_path).convert('RGB')
    img = img.resize(img_sze)
    arr_img = np.array(img)
    arr_img = np.expand_dims(arr_img, axis=0)
    arr_img_pre = preprocess_input(arr_img)

  except Exception as e:
    print(e)

  return arr_img_pre
