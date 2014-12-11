import os
from Trees.tree_classifier import *
from common.cross_validator import *


def read_data(dir_name, file_prefix):
    features = []
    labels = []
    with open(os.path.join(dir_name, file_prefix + ".data"), 'r') as f:
        for line in f.readlines():
            features.append([int(number) for number in line.split()])

    with open(os.path.join(dir_name, file_prefix + ".labels"), 'r') as f:
        labels = [int(number) for number in f.readlines()]

    return list(zip(features, labels))


classifier = TreeClassifier()
classifier.learn(read_data("./test", "arcene_train"))
result = calc_score(classifier, read_data("./test", "arcene_valid"), get_class_id=lambda x: x[1])
print(result.measure())
