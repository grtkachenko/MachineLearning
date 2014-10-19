from common.kernels import *
from common.point import Point
from smo import smo


class SVMClassifier:
    def __init__(self, kernel=dot):
        self.kernel = kernel
        self.train_data = []
        self.alpha, self.w, self.w0 = [], 0, 0

    def learn(self, train_data):
        self.train_data = train_data
        self.alpha, self.w0 = smo(1, 0, 10, train_data, self.kernel)
        self.w = Point(0, 0)
        lam, x = self.alpha, self.train_data
        for i in range(len(x)):
            self.w += x[i].mul_scalar(lam[i] * x[i].class_id)

    def get_class(self, test_point):
        res = self.kernel(self.w, test_point) + self.w0
        return 1 if res > 0 else 0

    def get_line(self):
        w = self.w
        k, b = -w.x/w.y, -self.w0/w.y
        return k, b