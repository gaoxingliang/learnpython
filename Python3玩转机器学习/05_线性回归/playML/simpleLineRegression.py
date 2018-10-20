import numpy as np


class SimpleLinearRegression1:
    def __init__(self):
        """初始化y=ax+b分别为None"""
        self.a_ = None
        self.b_ = None


    def fit(self, x_train, y_train):
        """目前只能处理1维的 所以要求2个都是1维的 而且要求他们的长度一样"""
        assert x_train.ndim == 1
        assert y_train.ndim == 1
        assert len(x_train) == len(y_train)

        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)
        fenzi = 0.0
        fenmu = 0.0
        for x, y in zip(x_train, y_train):
            fenzi += (x - x_mean) * (y - y_mean)
            fenmu += (x - x_mean) ** 2

        self.a_ = fenzi / fenmu
        self.b_ = y_mean - self.a_ * x_mean

        return self

    def predict(self, x_predict):
        """要求x是一个向量"""
        assert x_predict.ndim == 1
        assert self.a_ is not None and self.b_ is not None
        return np.array([self._predict(x) for x in x_predict])

    def _predict(self, x):
        return self.a_ * x + self.b_


    def __repr__(self):
        return "SimpleLinearRegression1"
