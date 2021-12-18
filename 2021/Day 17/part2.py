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
            x = ar[0].strip().split('=')[1].strip().split('..')
            y = ar[1].strip().split('=')[1].strip().split('..')

            x1 = int(x[0].strip())
            x2 = int(x[1].strip())

            y1 = int(y[0].strip())
            y2 = int(y[1].strip())

    def check(xx, yy):
        i = j = 0
        while i <= x2 and j >= y1:
            if x1 <= i <= x2 and y1 <= j <= y2:
                return True
            i += xx
            j += yy

            xx = max(0, xx - 1)
            yy -= 1
        return False

    max_height = abs(y1) * (abs(y1) - 1) // 2

    ans = 0
    for xx in range(1, x2 + 1):
        for yy in range(y1, max_height + 1):
            ans += check(xx, yy)

    return ans


for name in FILE_NAMES:
    print(name, solve(name))
