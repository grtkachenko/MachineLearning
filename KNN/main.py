from common.utils import normalize
from common.point import Point
from KNN.knn_classifier import *
from common.cross_validator import *

def optimal_k(chips):
    result = 0
    result_k = 1
    for k in range(1, min(20, len(chips))):
        cur = cross_validate(KnnClassifier(k), chips)
        print('with k = {} : result = {}'.format(k, cur.measure()))
        if cur.measure() > result:
            result = cur.measure()
            result_k = k
    return result_k

with open('chips.txt', 'r') as f:
    chips = [Point(*line.split(',')) for line in f.readlines()]
    chips = normalize(normalize(chips, 0), 1)
    shuffle(chips)
    count_to_test = len(chips)//5
    test = chips[:count_to_test]
    chips = chips[count_to_test:]
    k = optimal_k(chips)
    classifier = KnnClassifier(k)
    classifier.learn(chips)
    result = calc_score(classifier, test)
    print('optimal k = {}, measure = {}'.format(k, result.measure()))
