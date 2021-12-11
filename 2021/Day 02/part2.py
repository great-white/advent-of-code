YEAR = 2021
DAY = 'Day 02'
FILE_NAMES = ['small', 'large']


def solve(filename):
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            a, b = line.strip().split()
            ar.append((a, int(b)))

    x, y, aim = 0, 0, 0
    for key, val in ar:
        if key == 'forward':
            x += val
            y += val * aim
        if key == 'down':
            aim += val
        if key == 'up':
            aim -= val

    return x * y


for name in FILE_NAMES:
    print(name, solve(name))
