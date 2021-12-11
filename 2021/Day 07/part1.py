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

    N = max(ar) + 10

    for i in ar:
        d[i] += 1

    cur = ans = sum(ar)
    left, right = 0, len(ar)
    for i in range(N):
        right -= d[i]
        left += d[i]
        cur += left - right
        ans = min(ans, cur)
    return ans


for name in FILE_NAMES:
    print(name, solve(name))
