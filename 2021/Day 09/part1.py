YEAR = 2021
DAY = 'Day 09'
FILE_NAMES = ['small', 'large']


def solve(filename):
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(line)

    n, m = len(ar), len(ar[0])

    ans = 0
    X = [1, -1, 0, 0]
    Y = [0, 0, 1, -1]
    for i in range(n):
        for j in range(m):
            allLow = True
            for k in range(4):
                nx = i + X[k]
                ny = j + Y[k]
                if 0 <= nx < n and 0 <= ny < m:
                    allLow &= ar[i][j] < ar[nx][ny]
            if allLow:
                ans += int(ar[i][j]) + 1
    return ans


for name in FILE_NAMES:
    print(name, solve(name))
