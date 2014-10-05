from common.point import Point
from common.utils import normalize

with open('LinearDataset', 'f') as f:
    data = [Point(*(line.split(' '))) for line in f.readlines()]
    data = normalize(normalize(data, 0), 1)