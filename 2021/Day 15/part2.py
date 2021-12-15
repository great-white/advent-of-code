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

    n, m = len(ar), len(ar[0])

    def generate_grid(ar):
        new = []
        for i in range(n):
            mid = []
            for k in range(5):
                cur = []
                for j in range(m):
                    val = ar[i][j] + k
                    if val >= 10:
                        val -= 9
                    cur.append(val)
                mid.extend(cur)
            new.append(mid)

        mm = len(new)
        for k in range(1, 5):
            for i in range(n):
                cur = []
                for val in new[i]:
                    val = val + k
                    if val >= 10:
                        val -= 9
                    cur.append(val)
                new.append(cur)

        return new

    ar = generate_grid(ar)

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
