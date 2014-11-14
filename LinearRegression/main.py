import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

with open('prices.txt', 'r') as f:
    data = [list (line.split(',')) for line in f.readlines()]
    n = len(data)
    f = np.matrix([e[:2] + [1] for e in data]).astype(int)
    y = np.matrix([e[2] for e in data]).astype(int)
    a = (f.getT() * f).getI() * f.getT() * y.getT();
    result_measure = 0
    for i in range(0, n):
        result_measure += (y.item(i) - (f.item(i, 0) * a.item(0) + f.item(i, 1) * a.item(1) + a.item(2))) ** 2
    print(result_measure)
    print((result_measure / n) ** (1/2))
    print(a)

    point = np.array(data[0]).astype(int)
    normal = np.array([a.item(0), a.item(1), -1])
    d = -point.dot(normal) + a.item(2)

    mx = 5000
    xx, yy = np.meshgrid(range(0, mx + 1, mx // 2), range(10), sparse=True)
    z = (-normal[0] * xx - normal[1] * yy - d) * 1. / normal[2]

    fig = plt.figure()
    plt3d = fig.add_subplot(111, projection='3d')
    plt3d.plot_surface(xx, yy, z, alpha=0.2, color=[0,1,0])


    xs = []
    ys = []
    zs = []
    for cur in data :
        xs += [int(cur[0].strip())]
        ys += [int(cur[1].strip())]
        zs += [int(cur[2].strip())]

    plt3d.scatter(xs, ys, zs)
    # plt3d.scatter(f[:,0].tolist(), f[:,1].tolist(), y.tolist())
    plt.show()