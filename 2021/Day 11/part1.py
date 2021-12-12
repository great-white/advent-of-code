YEAR = 2021
DAY = 'Day 11'
FILE_NAMES = ['small', 'large']


def solve(filename):
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            cur = list(map(int, list(line)))
            ar.append(cur)

    n = len(ar)
    m = len(ar[0])

    def increment(ar):
        for i in range(n):
            for j in range(m):
                ar[i][j] += 1

    def countFlash(ar):
        ans = 0
        queue = []
        done = set()
        for i in range(n):
            for j in range(m):
                if ar[i][j] > 9:
                    queue.append([i, j])
                    done.add((i, j))

        X = [-1, -1, -1, 0, 0, 1, 1, 1]
        Y = [-1, 0, 1, -1, 1, -1, 0, 1]
        while queue:
            x, y = queue.pop(0)
            ans += 1
            for i in range(8):
                nx = x + X[i]
                ny = y + Y[i]
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in done:
                    ar[nx][ny] += 1
                    if ar[nx][ny] > 9:
                        queue.append([nx, ny])
                        done.add((nx, ny))

        for x, y in done:
            ar[x][y] = 0

        return ans

    ans = 0
    N = 100
    for i in range(N):
        increment(ar)
        ans += countFlash(ar)

    return ans


for name in FILE_NAMES:
    print(name, solve(name))
