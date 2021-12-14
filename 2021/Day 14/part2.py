from collections import defaultdict

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
                s = line
                continue
            if not line:
                continue
            pair, dest = line.split(' -> ')
            d[pair] = dest

    dp = defaultdict(int)
    for i in range(1, len(s)):
        dp[s[i-1:i+1]] += 1

    N = 40
    for _ in range(N):
        ndp = defaultdict(int)
        for key, value in dp.items():
            if key not in d:
                continue
            newVal = d[key]
            a = key[0] + newVal
            b = newVal + key[1]

            ndp[a] += value
            ndp[b] += value

        dp = ndp

    # print(dp)
    ans = defaultdict(int)
    mm, mn = 0, 10 ** 18
    for key, val in dp.items():
        ans[key[0]] += val
        ans[key[1]] += val

    for key in ans:
        ans[key] >>= 1
    ans[s[0]] += 1
    ans[s[-1]] += 1
    for key, val in ans.items():
        mm = max(mm, val)
        mn = min(mn, val)
    return mm - mn


for name in FILE_NAMES:
    print(name, solve(name))
