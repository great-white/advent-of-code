YEAR = 2021
DAY = 'Day 07'
FILE_NAMES = ['small', 'large']


def solve(filename):
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            ar = list(map(int, line.strip().split(',')))

    from collections import defaultdict
    d = defaultdict(int)

    N = max(ar) + 1

    ans = 10 ** 9
    for pos in range(N):
        cur = 0
        for i in ar:
            diff = abs(i - pos)
            cur += diff * (diff + 1) // 2
        ans = min(ans, cur)
    return ans


for name in FILE_NAMES:
    print(name, solve(name))
