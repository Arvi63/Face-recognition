import cv2
import time
from flask import Flask, request, jsonify, render_template, Response, make_response
# # from flask_cors import CORS
# from predict import predict_frame
# import base64
from flaskAPIHandler import APIHandler
application = Flask(__name__)
# CORS(application)
# application.debug = True

print("Loading api handler...")
api_handle = APIHandler()
print("Object of api handler created...", api_handle)

@application.route('/')
def index():
    # return 'index pages'
    return render_template('index.html')

def gen_video_stream():
    while True:
        frame = api_handle.predict_frame()
        ret, jpeg = cv2.imencode(".jpg", frame)
        frame_encode = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_encode + b'\r\n')

@application.route('/video_feed')
def video_feed():
    # print("Generator functi   on::",gen_video_stream())
    # return "Hello"
    return Response(gen_video_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == "__main__":
    application.run(host='0.0.0.0', port = '5001')

