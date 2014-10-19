from math import sqrt


def dot(p0, p1):
    return p0.x * p1.x + p0.y * p1.y


def dot_square(p0, p1):
    return dot(p0, p1)**2