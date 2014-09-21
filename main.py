from data import Data
from classifier import Classifier
from score import *
from validator import *

def optimal_k(chips):
    result = 0
    result_k = 1
    for k in range(1, len(chips)):
        cur = validate(chips, k)
        if cur.measure() > result:
            result = cur.measure()
            result_k = k
    return result_k

with open('chips.txt', 'r') as f:
    chips = [Data(*line.split(',')) for line in f.readlines()]
    shuffle(chips)
    count_to_test = len(chips)//5
    test = chips[:count_to_test]
    chips = chips[:count_to_test]
    k = optimal_k(chips)
    classifier = Classifier(k, chips)
    result = calc_score(classifier, test)
    print(result.measure())
