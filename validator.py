from random import shuffle
from score import *
from classifier import Classifier


def validate(train_data, k, blocks=5, times=10):
    cur_score = Score()
    for _ in range(0, times):
        shuffle(train_data)
        data_len = len(train_data)
        for __ in range(0, blocks):
            cur_score.add(calc_score(Classifier(k, train_data[data_len // blocks:data_len]), train_data[0:data_len // blocks]))
            train_data.rotate(data_len // blocks)

    return cur_score



