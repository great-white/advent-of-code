YEAR = 2021
DAY = 'Day 06'
FILE_NAMES = ['small', 'large']


def solve(filename):
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            ar = list(map(int, line.split(',')))

    dp = [0] * 9
    for i in ar:
        dp[i] += 1

    N = 80
    for i in range(N):
        zero = dp[0]
        for i in range(8):
            dp[i] = dp[i + 1]
        dp[8] = zero
        dp[6] += zero
    return sum(dp)


for name in FILE_NAMES:
    print(name, solve(name))
