import heapq

YEAR = 2021
DAY = 'Day 17'
FILE_NAMES = ['small', 'large']


def solve(filename):
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'

    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar = line.split(':')[1].strip().split(',')
            x = ar[0].strip().split('=')[1].strip().split('..')[0].strip()
            y = ar[1].strip().split('=')[1].strip().split('..')[0].strip()

    y = int(y)
    y = abs(y) - 1
    return y * (y + 1) // 2


for name in FILE_NAMES:
    print(name, solve(name))
