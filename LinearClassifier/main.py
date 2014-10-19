from common.point import Point
from svm_classifier import SVMClassifier
from common.score import *
from common.utils import *
from random import *

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.preprocessing import StandardScaler

with open('LinearDataset', 'r') as f:
    data = [Point(*(line.split(' '))) for line in f.readlines()]
    #data = [Point(-1, -2), Point(-1, 2), Point(1, 3, 1), Point(1, -1, 1)]
    shuffle(data)
    y = []
    for p in data:
        y.append(p.class_id)
    ratio = 0.8
    train_data, test_data = train_test_split(data, ratio)
    train_y, test_y = train_test_split(y, ratio)
    classifier = SVMClassifier()
    classifier.learn(train_data)
    result = calc_score(classifier, test_data)
    print('measure = {}'.format(result.measure()))

    figure = plt.figure(figsize=(14, 5))

    x_min, x_max = -10, 10
    y_min, y_max = -10, 10

    # just plot the dataset first
    cm = plt.cm.RdBu
    cm_bright = ListedColormap(['#FF0000', '#0000FF'])
    cm_bright_test = ListedColormap(['#00FF00', '#FFFFFF'])
    ax = plt.subplot(1, 2, 1)

    ax.scatter(*coords_arrays(train_data), c=train_y, cmap=cm_bright)
    # and testing points
    ax.scatter(*coords_arrays(test_data), c=test_y, cmap=cm_bright_test, alpha=1)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    # ax.set_xticks(())
    # ax.set_yticks(())
    #
    # # iterate over classifiers
    # for name, clf in zip(names, classifiers):
    #     ax = plt.subplot(len(datasets), len(classifiers) + 1, i)
    #     clf.fit(X_train, y_train)
    #     score = clf.score(X_test, y_test)
    #
    #     # Plot the decision boundary. For that, we will assign a color to each
    #     # point in the mesh [x_min, m_max]x[y_min, y_max].
    #     if hasattr(clf, "decision_function"):
    #         Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
    #     else:
    #         Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
    #
    #     # Put the result into a color plot
    #     Z = Z.reshape(xx.shape)
    #     ax.contourf(xx, yy, Z, cmap=cm, alpha=.8)
    #
    #     # Plot also the training points
    #     ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright)
    #     # and testing points
    #     ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright,
    #                alpha=0.6)
    #
    #     ax.set_xlim(xx.min(), xx.max())
    #     ax.set_ylim(yy.min(), yy.max())
    #     ax.set_xticks(())
    #     ax.set_yticks(())
    #     ax.set_title(name)
    #     ax.text(xx.max() - .3, yy.min() + .3, ('%.2f' % score).lstrip('0'),
    #             size=15, horizontalalignment='right')
    #     i += 1

    figure.subplots_adjust(left=.02, right=.98)
    k, b = classifier.get_line()
    print('k = {}, b = {}'.format(k, b))
    plt.plot([-10, 10], [-10 * k + b, 10 * k + b], 'k-');
    plt.show()
