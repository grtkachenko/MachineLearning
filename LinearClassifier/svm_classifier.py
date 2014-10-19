from common.kernels import *
from common.point import Point
from smo import Smo


class SVMClassifier:
    def __init__(self, kernel=dot):
        self.kernel = kernel
        self.train_data = []
        self.alpha, self.w, self.w0 = [], 0, 0

    def learn(self, train_data):
        self.train_data = train_data
        opt = Smo(2, 0, 5, self.kernel)
        self.alpha, self.w0 = opt.minimize(train_data)

    def get_w(self):
        w = Point(0, 0)
        lam, x = self.alpha, self.train_data
        for i in range(len(x)):
            y = 1 if x[i].class_id == 1 else -1
            w += x[i].mul_scalar(lam[i] * y)
        return w

    def get_class(self, test_point):
        res = 0
        lam, x = self.alpha, self.train_data
        for i in range(len(x)):
            y = 1 if x[i].class_id == 1 else -1
            res += self.kernel(x[i], test_point) * lam[i] * y
        res += self.w0
        return 1 if res > 0 else 0

    def get_line(self):
        w = self.get_w()
        k, b = -w.x/w.y, -self.w0/w.y
        return k, b