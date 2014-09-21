from data import Data
from random import shuffle
from classifier import Classifier
from score import *

def optimal_k(chips):
    return 2

with open('chips.txt', 'r') as f:
    chips = [Data(*line.split(',')) for line in f.readlines()]
    shuffle(chips)
    count_to_test = len(chips)/5
    test = chips[:count_to_test]
    chips = chips[:count_to_test]
    k = optimal_k(chips)
    classifier = Classifier(k, chips)

