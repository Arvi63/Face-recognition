from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from encoding import Encoding
encode = Encoding()

class Check_distance:

    # Using cosine similarity to compare features
    def cosine_check(self,feat):
        features, label, name = encode.load_feat()
        vect = []
        for items in [features]:
            result = cosine_similarity(items, feat)
            vect.append(result)
        ind = np.argmax(vect)
        return ind, np.max(vect),name

    # calculating euclidean distance between two features
    def euclid_check(self,feat):
        vect = []
        for items in features:
            result = np.linalg.norm(feat - items)
            vect.append(result)
        ind = np.argmin(vect)
        return ind,np.max(vect),name

