from common.point import Point
from svm_classifier import SVMClassifier
from common.score import *
from common.utils import *
from random import *

with open('LinearDataset', 'r') as f:
    data = [Point(*(line.split(' '))) for line in f.readlines()]
    data = normalize(normalize(data, 0), 1)
    shuffle(data)
    train_data, test_data = train_test_split(data, 0.8)
    classifier = SVMClassifier()
    classifier.learn(train_data)
    result = calc_score(classifier, test_data)
    print('measure = {}'.format(result.measure()))
    k, b = classifier.get_line()
    print('k = {}, b = {}'.format(k, b))
