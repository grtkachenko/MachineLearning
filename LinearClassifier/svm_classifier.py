from common.kernels import *
from smo import smo


class SVMClassifier:
    def __init__(self, kernel=dot):
        self.kernel = kernel
        self.train_data = []
        self.alpha, self.w0 = [], 0

    def learn(self, train_data):
        self.train_data = train_data
        self.alpha, self.w0 = smo(1, 1, 10, train_data, self.kernel)

    def get_class(self, test_point):
        res = 0
        lam, x = self.alpha, self.train_data
        for i in range(len(x)):
            res += lam[i] * x[i].class_id * self.kernel(x[i], test_point) - self.w0
        1 if res > 0 else 0

    def get_k(self):
        pass

    def get_b(self):
        pass