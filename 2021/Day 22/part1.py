from parse import parse
from collections import defaultdict


YEAR = 2021
DAY = 'Day 22'
FILE_NAMES = ['small-01', 'small-02', 'large']


def isValid(start: int, end: int) -> bool:
    return start >= -50 and end <= 50


def solve(filename):
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'
    cubes = dict()

    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            d = parse('{action} x={sx}..{ex},y={sy}..{ey},z={sz}..{ez}', line)
            d = d.named

            for key in d.keys():
                if key == 'action':
                    continue
                d[key] = int(d[key])

            if not isValid(d['sx'], d['ex']) or not isValid(d['sy'], d['ey']) or not isValid(d['sz'], d['ez']):
                continue

            for x in range(d['sx'], d['ex'] + 1):
                for y in range(d['sy'], d['ey'] + 1):
                    for z in range(d['sz'], d['ez'] + 1):
                        key = (x, y, z)
                        cubes[key] = d['action'] == 'on'

    return sum(cubes.values())


for name in FILE_NAMES:
    print(name, solve(name))
