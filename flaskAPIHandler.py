import cv2
import tensorflow as tf
# from prediction import Predict
# from train import Training
from flask import jsonify
import json
from face_detector import Face_detector
face_detect = Face_detector()
from flask import Flask,render_template
import sys
import csv
import datetime
import time
import pandas as pd


class APIHandler:
    def __init__(self):
 

        # Video Capture by OpenCV
        # self.capture = cv2.VideoCapture("rtsp://192.168.43.1:8080/h264_ulaw.sdp")
        self.capture = cv2.VideoCapture(0)
        self.img = None
        self.predictions = None

    def predict_frame(self, model):
        print("Running...")
        global roi
        ret, self.img = self.capture.read()
        print("ret",ret)
        if ret is True:
            print("Inside if")
            # Make image smaller for faster delivery
            frame = cv2.resize(self.img, None, fx=0.6, fy=0.6)
            print("frame ko shape:::", frame.shape)


            # print(ret)
            frame = cv2.flip(frame, 1)

            # self.predictions = self.predict.predict(X_img=frame, model_path=config.model_path)
            # frame, json_log, json_img = self.predict.show_prediction_labels_on_image(frame, self.predictions)

            # try:
            #     json_log = self.prediction.detected_image_log(self.predictions, self.img)
            # except(IndexError, UnboundLocalError):
            #     print(IndexError)
            # print("frame::", frame)


            threshold = 0.65
            roi,attendance = face_detect.haar_cascade_detector(frame,threshold,model)
            print("attendance system:::::",attendance)
            print("Attendance system ko type::",type(attendance))

            return roi,self.capture,attendance
        else:
            print("None and else condition")
            return None


    
       


       