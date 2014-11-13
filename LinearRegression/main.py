import numpy as np

with open('prices.txt', 'r') as f:
    data = [list (line.split(',')) for line in f.readlines()]
    f = np.matrix([e[:2] for e in data]).astype(int)
    y = np.matrix([e[2] for e in data]).astype(int)
    a = (f.getT() * f).getI() * f.getT() * y.getT();
    print(a)