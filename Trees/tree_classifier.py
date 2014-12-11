from Trees.node import *
from math import log2
from random import randint


class TreeClassifier:

    def __init__(self):
        pass

    def learn(self, train_data):
        self.tree = TreeClassifier.id3(train_data, 0)
        print(self.tree)

    @staticmethod
    def id3(data, height):
        if height >= 5:
            pos_tests, neg_tests = TreeClassifier.divide_list(data, lambda x: x[1] == 1)
            return Node(True, class_id=1 if len(pos_tests) > len(neg_tests) else -1)

        pos_tests, neg_tests = TreeClassifier.divide_list(data, lambda x: x[1] == 1)

        if len(pos_tests) == len(data):
            return Node(True, class_id=1)
        if len(neg_tests) == len(data):
            return Node(True, class_id=-1)


        cur_val = randint(0, 900)
        feature_num = max(range(0, len(data[0][0])), key=lambda x: TreeClassifier.gain(data, lambda y: y[0][x] > cur_val))
        predicate = lambda x: x[0][feature_num] > 0
        predicate_info = str(feature_num) + ' > 0'

        left_tests, right_tests = TreeClassifier.divide_list(data, predicate)
        res = Node(False, f=predicate, predicate_info=predicate_info)
        res.set_left(TreeClassifier.id3(left_tests, height + 1))
        res.set_right(TreeClassifier.id3(right_tests, height + 1))
        return res

    @staticmethod
    def divide_list(data, condition):
        pos = filter(lambda x: condition(x), data)
        neg = filter(lambda x: not condition(x), data)
        return list(pos), list(neg)

    @staticmethod
    def entropy(data, prop):
        m, n = len(TreeClassifier.divide_list(data, prop)[0]), len(data)
        n += 1
        m += 1
        a, b = m / n + 0.0001, (n - m) / n + 0.0001
        return - a * log2(a) - b * log2(b)

    @staticmethod
    def gain(data, prop):
        left, right = TreeClassifier.divide_list(data, prop)
        return TreeClassifier.entropy(data, prop) - TreeClassifier.entropy(left, prop) * len(left) / len(data) - \
               TreeClassifier.entropy(right, prop) * len(right) / len(data)

    def get_class(self, test_value):
        cur_node = self.tree
        while not cur_node.is_leaf:
            cur_node = cur_node.right if cur_node.f(test_value) else cur_node.left
        return cur_node.class_id
