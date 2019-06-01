from face_recog import Face_recog
import cv2
import dlib

from check_distance import Check_distance
check_dist = Check_distance()
face_rec = Face_recog()
class Face_detector:

    def haar_cascade_detector(self,image,threshold,inception_model):

        frame = image.copy()
        face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
        face_rects = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=3)
        if len(face_rects) >= 1:
            for (x, y, w, h) in face_rects:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 3)
                roi = frame[y:y + h, x:x + w]
                feat = face_rec.facenet_predict(roi,inception_model)
                re, sim_dist,name = check_dist.cosine_check(feat)
                if (sim_dist >= threshold):
                    cv2.putText(frame, str(name[re]), (x + 20, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                #         print("Face is::",name[re])
                else:
                    cv2.putText(frame, "Unknown face", (x + 20, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

        return frame

    def dlib_detector(self,image,threshold,inception_model):
        frame = image.copy()
        hog_face_detector = dlib.get_frontal_face_detector()
        face_rects = hog_face_detector(frame, 1)
        if len(face_rects) >= 1:
            for face in face_rects:
                x = face.left()
                y = face.top()
                w = face.right() - x
                h = face.bottom() - y
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 3)
                roi = frame[y:y + h, x:x + w]
                feat = face_rec.facenet_predict(roi,inception_model)
                re, sim_dist,name = check_dist.cosine_check(feat)
                if (sim_dist >= threshold):
                    cv2.putText(frame, str(name[re]), (x + 20, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                #         print("Face is::",name[re])
                else:
                    cv2.putText(frame, "Unknown face", (x + 20, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

        return frame

