YEAR = 2021
DAY = 'Day 01'
FILE_NAMES = ['small', 'large']


def solve(filename):
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(int(line))

    n = len(ar)
    ans = 0
    for i in range(1, n):
        ans += ar[i] > ar[i - 1]
    return ans


for name in FILE_NAMES:
    print(name, solve(name))
