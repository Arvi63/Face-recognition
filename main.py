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
from config import *
from query import *
from keras import backend as K
from keras.preprocessing import image
import tensorflow as tf
import glob
import os
import atexit
from werkzeug import secure_filename
from flask  import Flask,request,jsonify,render_template,Response,url_for,flash,redirect,session
# from keras.optimizers import RMSprop
import numpy as np
from vidgear.gears import VideoGear
# import matplotlib.pyplot as plt
# %matplotlib inline
import pandas as pd
import cv2
import dlib
# from add_image import ContactForm
import os.path
from flaskAPIHandler import APIHandler
import csv
import datetime
import time
api_handler = APIHandler()

from take_image import Take_img
take = Take_img()

from face_detector import Face_detector
from encoding import Encoding
from model import Model
encode = Encoding()
face_detect = Face_detector()
mod = Model()
# app = Flask(__name__)


app = Flask(__name__,
            static_url_path='', 
            static_folder='templates',
            template_folder='templates')


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
    global cap,attendance,full_attendance
    col_names = ['Name', 'Date', 'Time']
    full_attendance = pd.DataFrame(columns=col_names)
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
        try:
            with graph.as_default():

                    frame,cap,attendance = api_handler.predict_frame(mode)
                    print("fFramee::",attendance)
            if (attendance.empty == False):
                naam = attendance.iat[0, 0]
                dat = attendance.iat[0, 1]
                tim = attendance.iat[0, 2]
                full_attendance.loc[len(full_attendance)] = [naam, dat, tim]
            ret, jpeg = cv2.imencode(".jpg", frame)


            frame_encode = jpeg.tobytes()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame_encode + b'\r\n')
        except:
                print("Break from Recognition")
                new_attendance = full_attendance.drop_duplicates(subset=['Name'], keep='first')
                print("last ko:::::", new_attendance)
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                Hour, Minute, Second = timeStamp.split(":")
                fileName = "Attendance/Attendance_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
                new_attendance.to_csv(fileName, index=False)
                break
                
                

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

            folder_name = request.form['name']
            id = request.form['id']
            try:
                image = request.files['image']
            except:
                image = ''
            
            if folder_name.strip(' ')=='' or id.strip(' ')=='' or image == '' :
                flash('Please fill the form')
                return redirect(url_for('add_image'))

            else:
                
                itype = image.filename
                if itype.lower().endswith(('.png', '.jpg', '.jpeg')):
                    dataf = pd.read_csv('studentdups.csv')
                    if int(id) in dataf['ID'].values:
                        flash("Roll number already exist")
                        return redirect(url_for('add_image'))

                    else:
                        
                        new_name = folder_name+'_'+str(id)
                        myCsvRow = [[id,new_name]]
                        if os.path.isfile('studentdups.csv') == False:
                            myFile = open('studentdups.csv','w')
                            myData = [['ID','Name']]
                            with myFile:
                                writer = csv.writer(myFile)
                                writer.writerows(myData)

                        file = open('studentdups.csv','a')
                        with file:
                            writers = csv.writer(file)
                            writers.writerows(myCsvRow)

                        df = pd.read_csv('studentdups.csv')
                        a = df.drop_duplicates(subset=['Name'],keep='first')
                        a.to_csv('StudentDetails.csv')


                        if 'image' not in request.files:
                            flash('No file part')
                            return redirect(request.url)

                        files = request.files.getlist('image')
                        

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
                        for file in files:
                            # print("file::::",file)
                            filename = secure_filename(file.filename)

                            UPLOAD_FOLDER = face_folder
                            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
                            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                            
                            
                        return render_template('add_image.html')
                    


                else:
                    flash("File type should be image")
                    return redirect(url_for('add_image'))

    except: 
        print('Errors')
        return render_template('add_image.html')



@app.route('/stop_video',methods=['POST','GET'])
def stop_video():
    print(type(cap))
    cap.release()
    return redirect(url_for('temp'))
    # return render_template('index.html')

@app.route('/signup',methods=['POST','GET'])
def signup():
    return render_template('signup.html')

@app.route('/signup_post', methods=['POST','GET'])
def signup_post():
    username = request.form['username']
    name = request.form['name']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    if name.strip(' ')=="" or username.strip(' ')=='' or password.strip(' ') == '':
        flash('Please fill the form')
        return redirect(url_for('signup'))
    else:
        cu = check_username(username)
        if cu==1:
            flash('username already exist')
            return redirect(url_for('signup'))
        else:
            if password == confirm_password:
                a  = insert(username,name,password)
                if a==1:
                    flash("Data inserted successfully")
                else:
                    flash("Data insertion failed")
            else:
                flash("Password and Confirm password should match")

        return redirect(url_for('signup'))


@app.route('/loggedin', methods=['POST','GET'])
def loggedin():
    username = request.form['username']
    password = request.form['password']
    cu = check_username_password(username,password)

    if username.strip(' ')=="" or password.strip(' ')=='':
        flash("Please give both username and password to login")
        return redirect(url_for('temp'))

    else:
        if cu ==1:
            session['user']=username
            return redirect(url_for('after_login'))
        else:
            flash("Incorrect username or password")
            return redirect(url_for('temp'))


@app.route('/after_login', methods=['POST','GET'])
def after_login():
    if not session['user']:
        print("Please login before going forward")
        return redirect(url_for('temp'))
    else:
        print("session is present")
        return render_template('index0.html')

@app.route('/logout', methods=['POST','GET'])
def logout():
    session.pop('user',None)
    return redirect(url_for('temp'))


if __name__=='__main__':
    global graph
    # mode = mod.load_facenet_model()
    graph = tf.get_default_graph()
    # app.run(debug=True,port='5001')
    app.run(host='0.0.0.0', port='5000')




