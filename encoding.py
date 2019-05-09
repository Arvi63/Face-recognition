import os
import numpy as np
import string
class Encoding:
    def extract_feat(self):
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
                pred = adj_detect_face(string)
                features = np.append(features, pred, axis=0)
                label.append(a)
                sp = string.split('/')
                nam = sp[-2]
                name.append(nam)

            a = a + 1

        features = np.delete(features, 0, axis=0)
        print(features.shape)
        print(label)

        np.save('encoding', features)
        np.save('label', label)
        np.save('face_name', name)


    def load_feat(self):
        features = np.load('encoding.npy')
        label = np.load('label.npy')
        name = np.load('face_name.npy')
        return features,label,name
