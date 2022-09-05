import functools
import operator

import cv2
import numpy as np


def convertImageToRGBArray(img_path):
    img = cv2.imread(img_path)
    # Convert image to respective RGB color vector
    rgb_array = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return rgb_array


def getVectorFromImage(image_array):
    image_vector = np.reshape(a=image_array, newshape=(functools.reduce(operator.mul, image_array.shape)))
    return image_vector/255


def getImageFromVector(traits, image_shape):
    image_array = np.reshape(a=traits, newshape=image_shape)
    return image_array
