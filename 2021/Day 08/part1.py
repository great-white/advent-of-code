YEAR = 2021
DAY = 'Day 08'
FILE_NAMES = ['small', 'large']


def solve(filename):
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'
    with open(INPUT_PATH, 'r') as _file:
        dp = [2, 4, 3, 7]
        ans = 0
        for line in _file:
            cur = 0
            a, b = line.split(' | ')
            for i in b.split(' '):
                i = i.strip()
                ans += len(i) in dp

    return ans


for name in FILE_NAMES:
    print(name, solve(name))
