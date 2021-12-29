from typing import List
from parse import compile, parse


YEAR = 2021
DAY = 'Day 21'
FILE_NAMES = ['small', 'large']


def solve(filename):
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'
    positions = []
    scores = [0, 0]

    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            a = parse('Player {pid} starting position: {num}', line)
            positions.append(int(a['num']) - 1)

    init, idx = 1, 0
    while max(scores) < 1000:
        toAdd = 3 * init + 3
        positions[idx] += toAdd
        positions[idx] %= 10
        scores[idx] += positions[idx] + 1
        init += 3

        idx = (idx + 1) % 2

    return min(scores) * (init - 1)


for name in FILE_NAMES:
    print(name, solve(name))
