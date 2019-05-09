import cv2
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