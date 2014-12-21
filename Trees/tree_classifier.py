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
        pos_tests, neg_tests = TreeClassifier.divide_list(data, lambda x: x[1] == 1)
        # if height >= 3:
        #     return Node(True, class_id=1 if len(pos_tests) > len(neg_tests) else -1)

        if len(pos_tests) == len(data):
            return Node(True, class_id=1)
        if len(neg_tests) == len(data):
            return Node(True, class_id=-1)

        max_pred_val = cur_val = 0
        max_gain, max_feature_num = TreeClassifier.get_max_predicate(data, len(data[0][0]), cur_val)
        values_to_check = [20, 45, 80, 160, 300, 700]
        for i in range(0, 3):
            values_to_check.append(randint(0, 100))
        for i in range(0, 3):
            values_to_check.append(randint(100, 600))


        for cur_val in values_to_check:
            cur_gain, cur_feature_num = TreeClassifier.get_max_predicate(data, len(data[0][0]), cur_val)
            print(cur_gain, cur_val)
            if cur_gain > max_gain:
                max_gain, max_feature_num, max_pred_val = cur_gain, cur_feature_num, cur_val
        print('Optimal gain {} and predicate feature{} > {} ; Height = {}'.format(max_gain, max_feature_num, max_pred_val, height))
        predicate = lambda x: x[0][max_feature_num] > max_pred_val
        predicate_info = str(max_feature_num) + ' > ' + str(max_pred_val)

        left_tests, right_tests = TreeClassifier.divide_list(data, predicate)
        res = Node(False, f=predicate, predicate_info=predicate_info)
        res.set_left(TreeClassifier.id3(left_tests, height + 1))
        res.set_right(TreeClassifier.id3(right_tests, height + 1))
        return res

    @staticmethod
    def get_entropy_by_feature(data, total_feature_num):
        entropy_by_feature = {}
        for i in range(total_feature_num):
            value_cnt = {}
            for x in data:
                if x[0][i] not in value_cnt:
                    value_cnt[x[0][i]] = 1
                else:
                    value_cnt[x[0][i]] += 1
            ent = 0.0
            for key, value in value_cnt.items():
                a = value / len(data)
                ent += -a * log2(a)
            entropy_by_feature[i] = ent
        return entropy_by_feature

    @staticmethod
    def get_max_predicate(data, total_feature_num, pred_value):
        # entropy_by_feature = TreeClassifier.get_entropy_by_feature(data, total_feature_num)
        condition = lambda x: TreeClassifier.gain(data, lambda y: y[0][x] > pred_value)
        max_feature_num = max(range(0, total_feature_num), key=condition)
        return condition(max_feature_num), max_feature_num

    @staticmethod
    def divide_list(data, condition):
        pos = filter(lambda x: condition(x), data)
        neg = filter(lambda x: not condition(x), data)
        return list(pos), list(neg)

    @staticmethod
    def entropy(data):
        m, n = len(TreeClassifier.divide_list(data, lambda x: x[1] == 1)[0]), len(data)
        if m == 0 or n == m or n == 0:
            return 0
        a, b = m / n, (n - m) / n
        return - a * log2(a) - b * log2(b)

    @staticmethod
    def gain(data, prop):
        left, right = TreeClassifier.divide_list(data, prop)
        return TreeClassifier.entropy(data) - TreeClassifier.entropy(left) * len(left) / len(data) - \
               TreeClassifier.entropy(right) * len(right) / len(data)

    @staticmethod
    def gain_ratio(data, prop, feature_entropy):
        if feature_entropy == 0:
            return 0
        return TreeClassifier.gain(data, prop) / feature_entropy

    @staticmethod
    def gini_set(data):
        m, n = len(TreeClassifier.divide_list(data, lambda x: x[1] == 1)[0]), len(data)
        if n == 0:
            return 0
        return 1 - (m / n) ** 2 - ((n - m) / n) ** 2

    @staticmethod
    def gini(data, prop):
        left, right = TreeClassifier.divide_list(data, prop)
        return TreeClassifier.gini_set(data) - TreeClassifier.gini_set(left) * len(left) / len(data) - \
               TreeClassifier.gini_set(right) * len(right) / len(data)

    def get_class(self, test_value):
        cur_node = self.tree
        while not cur_node.is_leaf:
            cur_node = cur_node.right if cur_node.f(test_value) else cur_node.left
        return cur_node.class_id
