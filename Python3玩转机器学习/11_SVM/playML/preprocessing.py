import numpy as np

class StandardScaler:
    def __init__(self):
        self.mean_ = None
        self.scale_ = None

    def fit(self, X):
        assert X.ndim == 2, "now only support two dims"
        # 存储每一列的均值
        self.mean_ = np.array([np.mean(X[:, i]) for i in range(X.shape[1])])
        # 存储每一列的方差
        self.scale_ = np.array([np.std(X[:, i]) for i in range(X.shape[1])])
        return self

    def transform(self, X):
        """根据scale进行归一化处理"""
        assert X.ndim == 2, "now only support two dims"
        assert X.shape[1] == len(self.mean_)
        assert self.mean_ is not None, "must call fit"
        resX = np.empty(shape = X.shape, dtype=float)

        for col in range(X.shape[1]):
            # 标准化计算公式
            resX[:, col] = (X[:, col] - self.mean_[col])/self.scale_[col]

        return resX