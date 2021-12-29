from typing import List
from functools import lru_cache
from parse import parse


YEAR = 2021
DAY = 'Day 21'
FILE_NAMES = ['small', 'large']


@lru_cache(maxsize=None)
def fun(aPos: int, bPos: int, aScore: int, bScore: int, chance: int) -> List[int]:
    if aScore >= 21:
        return [1, 0]
    if bScore >= 21:
        return [0, 1]

    outcomes = [i + j + k for i in range(1, 4)
                for j in range(1, 4) for k in range(1, 4)]
    ans = [0, 0]
    if chance % 2 == 0:
        for outcome in outcomes:
            newPos = (aPos + outcome) % 10
            a, b = fun(newPos, bPos, aScore + newPos + 1, bScore, chance + 1)
            ans[0] += a
            ans[1] += b
    else:
        for outcome in outcomes:
            newPos = (bPos + outcome) % 10
            a, b = fun(aPos, newPos, aScore, bScore + newPos + 1, chance + 1)
            ans[0] += a
            ans[1] += b

    return ans


def solve(filename):
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'
    positions = []

    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            a = parse('Player {pid} starting position: {num}', line)
            positions.append(int(a['num']) - 1)

    a, b = fun(positions[0], positions[1], 0, 0, 0)
    return max(a, b)


for name in FILE_NAMES:
    print(name, solve(name))
