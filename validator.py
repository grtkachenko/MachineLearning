from random import shuffle
from score import *
from classifier import Classifier
from metrics import *


def rotate(l,n):
    return l[-n:] + l[:-n]


def validate(train_data, k, blocks=5, times=10):
    cur_score = Score()
    for _ in range(0, times):
        shuffle(train_data)
        data_len = len(train_data)
        for __ in range(0, blocks):
            pre_train_data = train_data[data_len // blocks:]
            pre_train_data_clone = list(pre_train_data)

            def num_diff(point):
                pre_train_data_clone.sort(key=lambda cur_point: euclidean(point, cur_point))
                num = 0
                for cur_point in pre_train_data_clone[1:k+1]:
                    if cur_point.class_id != point.class_id:
                        num += 1
                return -num

            pre_train_data.sort(key=lambda point: num_diff(point))
            start_index = 0
            # for p in pre_train_data:
            # if (abs(num_diff(p)) // 4) * 5 < k

            #     print(num_diff(p))
            # exit()

            cur_score.add(calc_score(Classifier(k, pre_train_data[20:]),
                                     train_data[:data_len // blocks]))
            rotate(train_data, data_len // blocks)

    return cur_score



