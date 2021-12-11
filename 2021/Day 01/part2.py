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
    for i in range(n - 3):
        a = sum(ar[i: i + 3])
        b = sum(ar[i + 1: i + 4])
        ans += b > a
    return ans


for name in FILE_NAMES:
    print(name, solve(name))
