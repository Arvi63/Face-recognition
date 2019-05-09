from keras.models import Sequential
from keras import models, layers
from keras import applications
from keras.applications.inception_v3 import InceptionV3
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten, Dense, Activation, Dropout
from keras.layers.normalization import BatchNormalization
from keras import Model
from keras import regularizers
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
import glob
from keras.optimizers import RMSprop
from keras.applications import inception_v3
import numpy as np
from vidgear.gears import VideoGear
# import matplotlib.pyplot as plt
# %matplotlib inline
import pandas as pd
import cv2
import dlib


from face_detector import Face_detector
from encoding import Encoding
from model import Model

face_detect = Face_detector()
mod = Model()

mode = mod.load_facenet_model()

threshold = 0.65
stream = VideoGear(source=0).start()

while True:
    frame = stream.read()
    roi = face_detect.haar_cascade_detector(frame,threshold,mode)

    cv2.imshow('frame', roi)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
stream.stop()



