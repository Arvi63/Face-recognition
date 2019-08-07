from face_recog import Face_recog
adj_det = Face_recog()
import os
import numpy as np
import string
# from face_detector import Face_detector
# face_detect = Face_detector()
class Encoding:

    def extract_feat(self,model,graph):
        features = np.zeros((1, 128))
        # label = np.zeros(1)
        a = 0
        label = []
        name = []
        gate = 'feature_image/'
        path = os.listdir(gate)
        for item in path:
            li = gate + item + '/'
            pa = os.listdir(li)
            for i in pa:
                string = li + i
                print(string)
                with graph.as_default():
                    pred = adj_det.adj_detect_face(string,model)
                    features = np.append(features, pred, axis=0)
                    label.append(a)
                    sp = string.split('/')
                    nam = sp[-2]
                    name.append(nam)

            a = a + 1

        features = np.delete(features, 0, axis=0)
        print(features.shape)
        print(label)

        np.save('test_encoding', features)
        np.save('test_label', label)
        np.save('test_face_name', name)


    def load_feat(self):
        features = np.load('test_encoding.npy')
        label = np.load('test_label.npy')
        name = np.load('test_face_name.npy')
        return features,label,name



