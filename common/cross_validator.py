from random import shuffle

from common.score import *


def rotate(l, n):
    return l[-n:] + l[:-n]


def cross_validate(classifier, train_data, blocks=5, times=10):
    cur_score = Score()
    for _ in range(0, times):
        shuffle(train_data)
        data_len = len(train_data)
        for __ in range(0, blocks):
            classifier.learn(train_data[data_len // blocks:])
            cur_score.add(calc_score(classifier, train_data[:data_len // blocks]))
            rotate(train_data, data_len // blocks)

    return cur_score



