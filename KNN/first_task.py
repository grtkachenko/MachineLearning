from common.utils import *
from common.cross_validator import *
from common.point import *
from LinearClassifier.svm_classifier import *
from matplotlib.patches import Ellipse
import matplotlib as plt
from matplotlib.colors import ListedColormap

with open('chips.txt', 'r') as f:
    chips = [Point(*line.split(',')) for line in f.readlines()]
    shuffle(chips)
    y = []
    for p in chips:
        y.append(p.class_id)
    ratio = 0.8
    train, test = train_test_split(chips, ratio)
    train_y, test_y = train_test_split(y, ratio)
    classifier = SVMClassifier(dot_square)
    classifier.learn(train)
    result = calc_score(classifier, test)
    print('measure = {}'.format(result.measure()))

    figure = plt.figure(figsize=(14, 5))

    x_min, x_max = -1, 1
    y_min, y_max = -1, 1

    # just plot the dataset first
    cm = plt.cm.RdBu
    cm_bright = ListedColormap(['#FF0000', '#0000FF'])
    cm_bright_test = ListedColormap(['#00FF00', '#FFFFFF'])
    ax = plt.subplot(1, 2, 1)

    ax.scatter(*coords_arrays(train), c=train_y, cmap=cm_bright)
    # and testing points
    ax.scatter(*coords_arrays(test), c=test_y, cmap=cm_bright_test, alpha=1)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
