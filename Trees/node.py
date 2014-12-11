class Node:
    def __init__(self, is_leaf, f=(lambda x: True), class_id=1, predicate_info=''):
        self.is_leaf = is_leaf
        self.f = f
        self.class_id = class_id
        self.left = None
        self.right = None
        self.predicate_info = predicate_info

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def __str__(self):
        return '(' + ('LEAF ' + str(self.class_id) if self.is_leaf else
                      'NODE ' + self.predicate_info + ' ' + self.left.__str__() + " " + self.right.__str__()) + ')'
