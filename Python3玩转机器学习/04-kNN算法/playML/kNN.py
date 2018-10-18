import numpy as np
from math import sqrt
from collections import Counter

class KNNClassifier:
    def __init__(self, k):
        assert k >=1; "k must be valid"
        self.k = k
        self._X_train = None
        self._y_train = None


    def fit(self, X_train, y_train):
        assert X_train.shape[0] == y_train.shape[0], "the size must be equal"
        self._X_train = X_train
        self._y_train = y_train
        return self

    def predict(self, X_predict):
        assert self._X_train is not None and self._y_train is not None, "should call fit"
        assert X_predict.shape[1] == self._X_train.shape[1], "feature number should be equal"
        y_predict = [self._predict(x) for x in X_predict]
        return np.array(y_predict)

    def _predict(self, x):
        distances = [sqrt(np.sum((x_train -x) ** 2)) for x_train in self._X_train]
        nearest = np.argsort(distances)
        topK_y = [self._y_train[i] for i in nearest[:self.k]]
        votes = Counter(topK_y)
        return votes.most_common(1)[0][0]


    def __repr__(self):
        return "KNN%d" % self.k