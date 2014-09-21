from metrics import *

class Classifier:
    def __init__(self, k, train_data, metrics=euclidean):
        self.k = k
        self.train_data = train_data
        self.metrics = metrics

    def get_class(self, test_point):
        self.train_data.sorted(key=lambda point: self.metrics(point, test_point))
        nearest_list = self.train_data[0:self.k]
        return nearest_list[0].class_id

