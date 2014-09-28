from KNN.data import Data
from common.validator import *


def optimal_k(chips):
    result = 0
    result_k = 1
    for k in range(1, min(20, len(chips))):
        cur = validate(chips, k)
        print('with k = {} : result = {}'.format(k, cur.measure()))
        if cur.measure() > result:
            result = cur.measure()
            result_k = k
    return result_k


def normalize(chips, coord_id):
    max_chip = max(chips, key=lambda p: abs(p.get(coord_id))).get(coord_id)

    def chip_fun(chip):
        if coord_id == 0:
            chip.x /= max_chip
        else:
            chip.y /= max_chip
        return chip
    return list(map(chip_fun, chips))

with open('chips.txt', 'r') as f:
    chips = [Data(*line.split(',')) for line in f.readlines()]
    chips = normalize(normalize(chips, 0), 1)
    shuffle(chips)
    count_to_test = len(chips)//5
    test = chips[:count_to_test]
    chips = chips[count_to_test:]
    k = optimal_k(chips)
    classifier = KnnClassifier(k, chips)
    result = calc_score(classifier, chips + test)
    print('optimal k = {}, measure = {}'.format(k, result.measure()))
