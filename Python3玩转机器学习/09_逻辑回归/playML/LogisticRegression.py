import numpy as np
from .metrics import accuracy_score
# 使用的是accuracy_score 因为我们面临的是一个分类问题了 我们关注的还是准确率

class LogisticRegression:
    def __init__(self):
        """初始化LogisticRegression回归"""
        # 系数
        self.coef_ = None
        # 截距
        self.interception_ = None
        self._theta = None

    def fit_normal(self, X_train, y_train):
        # 使用正规方程解的计算方式
        # LogisticRegression 没有方程解
        # assert X_train.shape[0] == y_train.shape[0], "样本数量必须一致"
        # X_b = np.hstack([np.ones((len(X_train), 1), dtype="float"), X_train])
        # self._theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y_train)
        # self._updateCoefAndInterception()
        assert False, "Not support"
        return self

    def _updateCoefAndInterception(self):
        self.interception_ = self._theta[0]
        self.coef_ = self._theta[1:]

    def _sigmoid(self, t):
        return 1./(1. + np.exp(-t))

    # rename from fit_gd because no sgd implemented
    def fit(self, X_train, y_train, eta = 0.01, n_iters=1e4):
        """采用梯度下降来训练LogisticRegression模型"""
        assert X_train.shape[0] == y_train.shape[0]
        # 此时X_train 并不包含截距
        # X_b 包含解决   theta 包含截距
        def J(theta, X_b, y):
            # 线性回归:计算损失函数 这里采用的是平方错误 也就是实际值 - 预测值   然后在平方
            # LogisticRegression 损失函数: 两部分求和

            try:
                y_hat = self._sigmoid(X_b.dot(theta))
                return -1. * np.sum(y*np.log(y_hat) + (1-y) * np.log(1-np.log(1 - y_hat)))/len(y)
            except:
                return float('inf')

        def dJ(theta, X_b, y):
            # 线性回归的梯度
            # return X_b.T.dot(X_b.dot(theta) - y) * 2. / len(X_b)

            # 逻辑回归的梯度
            return X_b.T.dot(self._sigmoid(X_b.dot(theta)) - y)  / len(X_b)

        def gd(X_b, y, initial_theta, eta, epsilon = 1e-8, n_iterations=1e4):
            n_iters = 0
            theta = initial_theta
            while n_iters < n_iterations:
                gradient = dJ(theta, X_b, y)
                lastTheta = theta
                # 每一次迭代 向梯度的相反方向更新theta
                theta = theta - eta * gradient
                # 是否达到额定的误差
                if abs(J(lastTheta, X_b, y) - J(theta, X_b, y)) < epsilon:
                    break
                n_iters += 1
            return theta

        # 添加一个截距列 方便后面计算
        # X_train 是 m * n  比如  [
        #    [1, 2, 3]
        #    [4, 5, 6]
        # ]
        # X_b 是 m * (n + 1)
        # [
        #    [1, 1, 2, 3]
        #    [1, 4, 5, 6]
        # ]

        X_b = np.hstack((np.ones((len(X_train), 1)), X_train))
        y = y_train

        initial_theta = np.zeros(X_b.shape[1])
        self._theta = gd(X_b, y, initial_theta, eta, n_iterations= n_iters)
        #print("theta calculated", self._theta)
        self._updateCoefAndInterception()
        return self

    def predict_proba(self, X_predict):
        # 给定待预测的值, 返回他的概率
        assert self.coef_ is not None
        assert X_predict.shape[1] == len(self.coef_)
        X_b = np.hstack([np.ones((len(X_predict), 1)), X_predict])
        return self._sigmoid(X_b.dot(self._theta))



    def predict(self, X_predict):
        proba = self.predict_proba(X_predict)
        # True ->1 False->0
        return np.array(proba >= 0.5, dtype="int")

    def score(self, X_test, y_test):
        y_predict = self.predict(X_test)
        return accuracy_score(y_test, y_predict)

    def __repr__(self):
        return "LogisticRegression()"