from metrics import *
from data import Data

class Classifier:
    def __init__(self, k, train_data, metrics=euclidean):
        self.k = k
        self.train_data = train_data
        self.metrics = metrics

    def get_class(self, test_point):
        self.train_data.sort(key=lambda point: self.metrics(point, test_point))
        nearest_list = self.train_data[0:self.k]
        class_dict = dict()
        for point in nearest_list:
            if not point.class_id in class_dict:
                class_dict[point.class_id] = 0
            class_dict[point.class_id] += 1 / self.metrics(point, test_point)

        return max(class_dict, key=class_dict.get)
