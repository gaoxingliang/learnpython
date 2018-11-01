import numpy as np
from .metrics import r2_score

class LinearRegression:
    def __init__(self):
        """初始化多元线性回归"""
        # 系数
        self.coef_ = None
        # 截距
        self.interception_ = None
        self._theta = None

    def fit_normal(self, X_train, y_train):
        # 使用正规方程解的计算方式
        assert X_train.shape[0] == y_train.shape[0], "样本数量必须一致"
        X_b = np.hstack([np.ones((len(X_train), 1), dtype="float"), X_train])
        self._theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y_train)
        self._updateCoefAndInterception()
        return self

    def fit_normal_pesudo_inv(self, X_train, y_train):
        # 使用正规方程解的计算方式 看看伪逆矩阵计算应该是一致的
        assert X_train.shape[0] == y_train.shape[0], "样本数量必须一致"
        X_b = np.hstack([np.ones((len(X_train), 1), dtype="float"), X_train])
        self._theta = np.linalg.pinv(X_b).dot(y_train)
        self._updateCoefAndInterception()
        return self

    def _updateCoefAndInterception(self):
        self.interception_ = self._theta[0]
        self.coef_ = self._theta[1:]

    def fit_gd(self, X_train, y_train, eta = 0.01, n_iters=1e4):
        """采用梯度下降来训练线性回归模型"""
        assert X_train.shape[0] == y_train.shape[0]
        # 此时X_train 并不包含截距
        # X_b 包含解决   theta 包含截距
        def J(theta, X_b, y):
            # 计算损失函数 这里采用的是平方错误 也就是实际值 - 预测值   然后在平方
            try:
                return np.sum((y - X_b.dot(theta)) ** 2) / len(y)
            except:
                return float('inf')

        def dJ(theta, X_b, y):
            # 计算偏导数 也就是梯度
            # 方法1: 直接根据定义计算
            # res = np.empty(len(theta))
            # # 截距b的偏导数
            # res[0] = np.sum(X_b.dot(theta) - y)
            #
            # # 对其他特征一个个计算 参考公式
            # for i in range(1, len(theta)):
            #     res[i] = np.sum((X_b.dot(theta) - y).dot(X_b[:, i])) / len(y_train)
            # return res

            # 方法2 直接向量化计算
            return X_b.T.dot(X_b.dot(theta) - y) * 2. / len(X_b)


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


    # SGD
    # a, b 用来计算eta 的值 随着迭代次数越来越小
    def fit_sgd(self, X_train, y_train, n_iters=5, a=5, b = 50):
        assert len(X_train) == len(y_train)
        assert n_iters >= 1

        def dJ_sgd(theta, X_b_i, y_i):
            # X_b_i 代表第i个样本  y_i 代表数据值
            return X_b_i.T.dot(X_b_i.dot(theta) - y_i) * 2.

        def sgd(X_b, y, initial_theta, n_iters, a, b):
            a = 5
            b = 50

            def learning_rate(iter):
                return a / (b + iter)

            # 因为我们是随机梯度下降 所以一般的话 我们至少要保证每个都看一遍
            # 所以在sgd 中n_iters 一般表示所有数据最多看多少遍

            # 现在是随机选一个点 可能这2个点隔的很近 所以epsilon 已经没有意义了
            m = len(X_b)
            theta = initial_theta
            for cur_iter in range(n_iters):
                # 为了保证每个都看过 所以我们打乱这个原来的X_b
                indexes = np.random.permutation(m)
                X_b_new = X_b[indexes]
                y_new = y[indexes]
                for i in range(m):
                    gradient = dJ_sgd(theta, X_b_new[i], y_new[i])
                    theta = theta - learning_rate(cur_iter * m + i) * gradient
            return theta

        X_b = np.hstack((np.ones((len(X_train), 1)), X_train))
        initial_theta = np.zeros(X_b.shape[1])
        # 这里只是举例取1/3的数据
        self._theta = sgd(X_b, y_train, initial_theta, n_iters, a, b)
        self._updateCoefAndInterception()
    # SGD



    def predict(self, X_predict):
        assert self.coef_ is not None
        assert X_predict.shape[1] == len(self.coef_)
        X_b = np.hstack([np.ones((len(X_predict), 1)), X_predict])
        return X_b.dot(self._theta)

    def score(self, X_test, y_test):
        y_predict = self.predict(X_test)
        return r2_score(y_test, y_predict)

    def __repr__(self):
        return "LinearRegression()"