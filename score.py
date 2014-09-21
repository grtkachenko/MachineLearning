class Score:
    def __init__(self, TP=0, TN=0, FP=0,FN=0):
        self.TP = TP
        self.TN = TN
        self.FP = FP
        self.FN = FN

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