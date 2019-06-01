# from keras.models import Sequential
# from keras import models, layers
# from keras import applications
# from keras.applications.inception_v3 import InceptionV3
# from keras.layers import Conv2D
# from keras.layers import MaxPooling2D
# from keras.layers import Flatten, Dense, Activation, Dropout
# from keras.layers.normalization import BatchNormalization
# from keras import Model
# from keras import regularizers
# from keras.preprocessing.image import ImageDataGenerator
from keras import backend as K
from keras.preprocessing import image
import glob
from flask  import Flask,request,jsonify,render_template
# from keras.optimizers import RMSprop
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
encode = Encoding()
face_detect = Face_detector()
mod = Model()
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def temp():
    return render_template('index.html')

@app.route('/feat',methods=['GET','POST'])
def feature():
    tracker = encode.extract_feat(mode)


@app.route('/upload',methods=['GET','POST'])
def recognize():
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
    K.clear_session()

    return "thanks for trying"

if __name__=='__main__':
    app.run(debug=True,port='5000')




