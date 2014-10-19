from math import sqrt


def dot(p0, p1):
    return sqrt((p0.x - p1.x)**2 + (p0.y - p1.y)**2)


def dot_square(p0, p1):
    return (p0.x - p1.x)**2 + (p0.y - p1.y)**2