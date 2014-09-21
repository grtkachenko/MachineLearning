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
        return self.TP / (self.TP + self.FP)

    def recall(self):
        return self.TP / (self.TP + self.FN)

    def measure(self):
        return 2 * self.precission() * self.recall() / (self.precission() + self.recall())


def calc_score(classifier, test_data):
    return Score()