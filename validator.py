from random import shuffle
from score import *


def validate(classifier, train_data, blocks, times):
    cur_score = Score()
    for _ in range(0, times):
        shuffle(train_data)
        data_len = len(train_data)
        for __ in range(0, blocks):
            cur_score.add(calc_score(classifier, train_data[0:data_len // blocks]))
            train_data.rotate(data_len // blocks)

    return cur_score



