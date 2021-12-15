import heapq

YEAR = 2021
DAY = 'Day 15'
FILE_NAMES = ['small', 'large']


def solve(filename):
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []

    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            cur = list(map(int, list(line)))
            ar.append(cur)

    heap = [(0, 0, 0)]
    X = [0, 0, 1, -1]
    Y = [1, -1, 0, 0]
    n, m = len(ar), len(ar[0])

    done = set()
    while heap:
        cost, x, y = heapq.heappop(heap)
        if (x, y) in done:
            continue
        done.add((x, y))

        if x == n - 1 and y == m - 1:
            return cost

        for i in range(4):
            nx = x + X[i]
            ny = y + Y[i]

            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in done:
                heapq.heappush(heap, (cost + ar[nx][ny], nx, ny))
    return -1


for name in FILE_NAMES:
    print(name, solve(name))
