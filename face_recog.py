import cv2
import dlib
import numpy as np
class Face_recog:

    # for face-rec-google model
    def google_predict(self,imag,inception_model):
        #     img = image.load_img(imag,target_size=(96,96))
        #     img = image.img_to_array(img)
        img = imag
        img = cv2.resize(img, (96, 96))
        img = img / 255
        tr_img = img.transpose((2, 1, 0))
        tr_img = np.expand_dims(tr_img, axis=0)
        pred_feature = inception_model.predict(tr_img)
        return pred_feature


    # for facenet model
    def facenet_predict(self,imag,inception_model):
        #     img = image.load_img(imag,target_size=(96,96))
        #     img = image.img_to_array(img)
        img = imag
        img = cv2.resize(img, (160, 160))
        img = img / 255
        #     tr_img = img.transpose((2, 1, 0))
        tr_img = np.expand_dims(img, axis=0)
        pred_feature = inception_model.predict(tr_img)
        return pred_feature


    def adj_detect_face(self,img,model):
        img = cv2.imread(img)
        face_img = img.copy()
        roi = img.copy()
        hog_face_detector = dlib.get_frontal_face_detector()
        face_rects = hog_face_detector(face_img, 1)
        for face in face_rects:
            #         cv2.rectangle(face_img, (x,y), (x+w,y+h), (255,255,255), 10)
            x = face.left()
            y = face.top()
            w = face.right() - x
            h = face.bottom() - y
            roi = roi[y:y + h, x:x + w]
            #         print(roi.shape)
            feat = self.facenet_predict(roi,model)
        return feat
    #         plt.imshow(roi)
    #     return (x,y,w,h)
