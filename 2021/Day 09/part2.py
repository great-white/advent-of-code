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
    for i in range(n):
        ar[i] = list(ar[i])

    def dfs(x, y):
        if x < 0 or x >= n or y < 0 or y >= m:
            return 0
        if ar[x][y] in ['#', '9']:
            return 0
        ar[x][y] = '#'
        X = [1, -1, 0, 0]
        Y = [0, 0, 1, -1]
        ans = 1
        for i in range(4):
            nx = x + X[i]
            ny = y + Y[i]
            ans += dfs(nx, ny)
        return ans

    cur = []
    for i in range(n):
        for j in range(m):
            if ar[i][j] in ['9', '#']:
                continue
            cur.append(dfs(i, j))
    cur.sort(reverse=True)
    ans = 1
    for i in cur[0:3]:
        ans *= i
    return ans


for name in FILE_NAMES:
    print(name, solve(name))
