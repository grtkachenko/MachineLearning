import numpy as np
from common.utils import *
from common.cross_validator import *
from common.point import *
from LinearClassifier.svm_classifier import *
from matplotlib.patches import Ellipse
import matplotlib.pyplot as plt
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

    figure = plt.figure(figsize=(14, 14))

    x_min, x_max = -1.5, 1.5
    y_min, y_max = -1.5, 1.5

    h = 0.05
    xx, yy = np.arange(x_min, x_max, h), np.arange(y_min, y_max, h)
    mesh_pts = []
    mesh_y = []
    for xi in xx:
        for yi in yy:
            pt = Point(xi, yi)
            mesh_pts.append(pt)
            mesh_y.append(classifier.get_class(pt))

    print(mesh_y)
    # just plot the dataset first
    cm = plt.cm.RdBu
    cm_bright = ListedColormap(['#FF0000', '#0000FF'])
    cm_bright_test = ListedColormap(['#00FF00', '#FFFFFF'])
    ax = plt.subplot()

    ax.scatter(*coords_arrays(mesh_pts), c=mesh_y, cmap=cm_bright, marker=',')
    #ax.scatter(*coords_arrays(train), c=train_y, cmap=cm_bright)
    # and testing points
    #ax.scatter(*coords_arrays(test), c=test_y, cmap=cm_bright_test, alpha=1)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    plt.show()
