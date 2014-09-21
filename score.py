class Score:
    def __init__(self, tp=0, tn=0, fp=0, fn=0):
        self.TP = tp
        self.TN = tn
        self.FP = fp
        self.FN = fn

    def add(self, other):
        self.TP += other.TP
        self.TN += other.TN
        self.FP += other.FP
        self.FN += other.FN
        return self

    def precission(self):
        denom = self.TP + self.FP
        if denom == 0:
            return 0
        return self.TP / denom

    def recall(self):
        denom = (self.TP + self.FN)
        if denom == 0:
            return 0
        return self.TP / denom

    def measure(self):
        denom = self.precission() + self.recall()
        if denom == 0:
            return 0
        return 2 * self.precission() * self.recall() / denom


def calc_score(classifier, test_data):
    score = Score()
    for test in test_data:
        supposed_id = classifier.get_class(test)
        if test.class_id == supposed_id:
            if test.class_id == 1:
                score.TP += 1
            else:
                score.TN += 1
        else:
            if test.class_id == 1:
                score.FP += 1
            else:
                score.FN += 1
    return score
