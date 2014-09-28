from random import shuffle

from common.score import *
from KNN.knn_classifier import KnnClassifier


def rotate(l,n):
    return l[-n:] + l[:-n]


def validate(train_data, k, blocks=5, times=10):
    cur_score = Score()
    for _ in range(0, times):
        shuffle(train_data)
        data_len = len(train_data)
        for __ in range(0, blocks):
            cur_score.add(calc_score(KnnClassifier(k, train_data[data_len // blocks:]),
                                     train_data[:data_len // blocks]))
            rotate(train_data, data_len // blocks)

    return cur_score



