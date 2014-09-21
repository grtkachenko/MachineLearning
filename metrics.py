from math import sqrt


def euclidean(p0, p1):
    k = 2
    return (abs((p0.x - p1.x)**k) + abs((p0.y - p1.y)**k))**(1/k)