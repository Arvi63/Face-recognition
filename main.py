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
import tensorflow as tf
import glob
import os

from werkzeug import secure_filename
from flask  import Flask,request,jsonify,render_template,Response,url_for,flash,redirect
# from keras.optimizers import RMSprop
import numpy as np
from vidgear.gears import VideoGear
# import matplotlib.pyplot as plt
# %matplotlib inline
import pandas as pd
import cv2
import dlib
# from add_image import ContactForm

from flaskAPIHandler import APIHandler
api_handler = APIHandler()

from take_image import Take_img
take = Take_img()

from face_detector import Face_detector
from encoding import Encoding
from model import Model
encode = Encoding()
face_detect = Face_detector()
mod = Model()
app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/',methods=['GET','POST'])
def temp():
    return render_template('index.html')

@app.route('/feat',methods=['GET','POST'])
def feature():
    tracker = encode.extract_feat(mode,graph)
    return render_template('index.html')


@app.route('/recognition',methods=['GET','POST'])
def recognition():
    return render_template('index1.html')


# def capture():
#     # capture = cv2.VideoCapture(0)
#     capture = VideoGear(source=0).start()
#     ret, frame = capture.read()
#     if ret is True:
#         frame = cv2.flip(frame, 1)
#         framee = cv2.resize(frame, None, fx=0.6, fy=0.6)
#     return framee


def gen():
    # stream = VideoGear(source=0).start()
    global cap
    while True:
        # capture = cv2.VideoCapture(0)
        # ret, frame = capture.read()
        # if ret is True:
            # mode = mod.load_facenet_model()
            # threshold = 0.65
            # frame = stream.read()
            # roi = face_detect.haar_cascade_detector(frame,threshold,mode)
            # frame = cv2.resize(frame, None, fx=0.6, fy=0.6)
        # global graph
        with graph.as_default():    
            try:
                frame,cap = api_handler.predict_frame(mode)
            except:
                print("Break from Recognition")
                break
        ret, jpeg = cv2.imencode(".jpg", frame)


        frame_encode = jpeg.tobytes()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame_encode + b'\r\n')


@app.route('/recognize')
def recognize():

    # stream = VideoGear(source=0).start()
    #
    # while True:
    #     frame = stream.read()
    #     roi = face_detect.haar_cascade_detector(frame,threshold,mode)
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

    #     cv2.imshow('frame', roi)
    #     if cv2.waitKey(1) & 0xFF == 27:
    #         break
    #
    # cv2.destroyAllWindows()
    # stream.stop()
    # K.clear_session()
    #
    # return "thanks for trying"



@app.route('/add_image',methods=['GET','POST'])
def add_image():
    return render_template('add_image.html')


def create_folder(folder_name):
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)


# @app.route('/form',methods=['POST','GET'])
# def form():
#     form = ContactForm()
#     if request.method == 'POST':
        
#         if form.validate() == False:
#             flash('All fields are required.')
#             return render_template('add_image.html', form = form)
#         else:
#             # return render_template('success.html')
#             flash("form validated")


    
@app.route('/add_image_form',methods=['POST','GET'])
def add_image_form():
    try:

        # form = ContactForm()
        if request.method == 'POST':
            # if form.validate() == False:
            #     flash('All fields are required.')
            #     return render_template('add_image.html', form = form)
            # else:
            #     # return render_template('success.html')
            #     flash("form validated")



            FACE_DIR = "feature_image/"

            print("hello world 2")
            folder_name = request.data
            print(folder_name)
            id = request.get_json()
            print(id)


            image = request.files['image']
            print('folder name')
            print(folder_name)


            
            create_folder(FACE_DIR)

            while True:
                    
                    try:
                        face_id = int(id)
                        face_folder = FACE_DIR + folder_name+'_'+str(id) + "/"
                        create_folder(face_folder)
                        break
                    except:
                        print("Invalid input. id must be int")
                        continue
            filename = secure_filename(image.filename)

            UPLOAD_FOLDER = face_folder
            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            
            return render_template('add_image.html')
    except:
        print('Errors')
        return render_template('add_image.html')



@app.route('/stop_video',methods=['POST','GET'])
def stop_video():
    print(type(cap))
    cap.release()
    # return redirect(url_for('temp'))
    return render_template('index.html')








if __name__=='__main__':
    global graph
    mode = mod.load_facenet_model()
    graph = tf.get_default_graph()
    # app.run(debug=True,port='5001')
    app.run(host='0.0.0.0', port='5000')




