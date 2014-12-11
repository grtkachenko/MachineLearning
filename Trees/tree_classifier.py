from Trees.node import *
from random import randint


class TreeClassifier:

    def __init__(self):
        pass

    def learn(self, train_data):
        self.tree = TreeClassifier.id3(train_data, 0)

    @staticmethod
    def id3(data, height):
        if height >= 3:
            return Node(True, class_id=1 if randint(0, 1) == 1 else -1)

        pos_tests, neg_tests = TreeClassifier.divide_list(data, lambda x: x[1] == 1)

        if len(pos_tests) == len(data):
            return Node(True, class_id=1)
        if len(neg_tests) == len(data):
            return Node(True, class_id=-1)

        # TODO: replace with correct predicate selection
        feature_num = randint(0, len(data[0][0]) - 1)
        predicate = lambda x: x[0][feature_num] > 30
        predicate_info = str(feature_num) + ' > 30'

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

    def get_class(self, test_value):
        cur_node = self.tree
        while not cur_node.is_leaf:
            cur_node = cur_node.right if cur_node.f(test_value) else cur_node.left
        return cur_node.class_id
