from data import Data

with open('chips.txt', 'r') as f:
    chips = [Data(*line.split(',')) for line in f.readlines()]
    for chip in chips:
        print(chip)