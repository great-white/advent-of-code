YEAR = 2021
DAY = 'Day 05'
FILE_NAMES = ['small', 'large']


def solve(filename):
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'
    ar = [[0] * 1000 for _ in range(1000)]
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            a, b = line.split(' -> ')
            x1, y1 = map(int, a.split(','))
            x2, y2 = map(int, b.split(','))
            if x1 == x2:
                for i in range(min(y1, y2), max(y1, y2) + 1):
                    ar[x1][i] += 1
            elif y1 == y2:
                for i in range(min(x1, x2), max(x1, x2) + 1):
                    ar[i][y1] += 1
            else:
                ix = 1 if x2 > x1 else -1
                iy = 1 if y2 > y1 else -1
                while x1 != x2:
                    ar[x1][y1] += 1
                    x1 += ix
                    y1 += iy
                ar[x1][y1] += 1

    ans = 0
    for row in ar:
        for i in row:
            ans += i > 1
    return ans


for name in FILE_NAMES:
    print(name, solve(name))
