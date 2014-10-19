from common.point import Point
from common.utils import normalize
from smo import smo

data = []

with open('LinearDataset', 'r') as f:
    data = [Point(*(line.split(' '))) for line in f.readlines()]
    data = normalize(normalize(data, 0), 1)

a, b = smo(1, 1, 1, data)
