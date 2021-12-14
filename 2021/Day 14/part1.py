from collections import Counter

YEAR = 2021
DAY = 'Day 14'
FILE_NAMES = ['small', 'large']


def solve(filename):
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'
    s = []
    d = dict()
    with open(INPUT_PATH, 'r') as f:
        for line in f:
            line = line.strip()
            if not s:
                s = list(line)
                continue
            if not line:
                continue
            pair, dest = line.split(' -> ')
            d[pair] = dest

    N = 10
    for _ in range(N):
        n = len(s)
        insertions = []
        for i in range(1, n):
            cur = ''.join(s[i-1:i+1])
            insertions.append([i, d[cur]])
        for idx, char in insertions[::-1]:
            s.insert(idx, char)

    d = Counter(s)
    mm, mn = 0, 10 ** 9
    for key, val in d.items():
        mm = max(mm, val)
        mn = min(mn, val)
    return mm - mn


for name in FILE_NAMES:
    print(name, solve(name))
