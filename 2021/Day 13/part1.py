YEAR = 2021
DAY = 'Day 13'
FILE_NAMES = ['small', 'large']


def solve(filename):
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'
    LIMIT = 0
    dots, folds = [], []
    n = m = LIMIT
    with open(INPUT_PATH, 'r') as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue
            if line.startswith('fold'):
                cur = line.split()[2].split('=')
                cur[1] = int(cur[1]) + LIMIT
                folds.append(cur)
            else:
                cur = list(map(int, line.split(',')))
                cur[0] += LIMIT
                cur[1] += LIMIT
                dots.append(cur[::-1])
                n = max(n, cur[1] + LIMIT) + 1
                m = max(m, cur[0] + LIMIT) + 1

    ar = [['.'] * (m + 1) for _ in range(n + 1)]
    for x, y in dots:
        ar[x][y] = '#'

    def processFold(dim, num):
        if dim == 'y':
            row1, row2 = num - 1, num + 1

            while row1 >= 0 and row2 < n:
                for j in range(m):
                    if ar[row1][j] == '#' or ar[row2][j] == '#':
                        ar[row1][j] = '#'
                    ar[row2][j] = '.'
                row1 -= 1
                row2 += 1
        else:
            col1, col2 = num - 1, num + 1

            while col1 >= 0 and col2 < m:
                for i in range(n):
                    if ar[i][col1] == '#' or ar[i][col2] == '#':
                        ar[i][col1] = '#'
                    ar[i][col2] = '.'
                col1 -= 1
                col2 += 1

    processFold(folds[0][0], folds[0][1])

    ans = 0
    for i in range(n):
        for j in range(m):
            ans += ar[i][j] == '#'
    return ans


for name in FILE_NAMES:
    print(name, solve(name))
