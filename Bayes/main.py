import os
import itertools
from Bayes.msg import Message
from Bayes.bayes_classifier import BayesClassifier
from common.score import *

test_dir = "./test"
data = []
for data_part in os.listdir(test_dir):
    for root, _, files in os.walk(os.path.join(test_dir, data_part)):
        msgs = []
        for file in files:
            with open(os.path.join(root, file), 'r') as f:
                lines = [line for line in f.readlines()]
                subject = [int(number) for number in lines[0].split()[1:]]
                body = [int(number) for number in lines[2].split()]
                msgs.append(Message(subject, body, 0 if "spmsg" in file else 1))
        data.append(msgs)

study = list(itertools.chain(*data[:-1]))
test = data[-1]
classifier = BayesClassifier(study)
result = calc_score(classifier, test)
print(result.measure())