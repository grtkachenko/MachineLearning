import os
import itertools
from Bayes.msg import Message
from Bayes.bayes_classifier import BayesClassifier
from common.score import *

test_dir = "./test"

data = []
labels = []
with open(os.path.join(test_dir, "arcene_train.data"), 'r') as f:
    for line in f.readlines():
        data.append([int(number) for number in line.split()])

with open(os.path.join(test_dir, "arcene_train.labels"), 'r') as f:
    labels = [int(number) for number in f.readlines()]

