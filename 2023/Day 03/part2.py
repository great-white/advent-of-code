import os
from collections import defaultdict

FILE_NAMES = ['small', 'large']
symbolMap = defaultdict(list)


def issymbol(ar, x, y):
    return ar[x][y] == '*'


def findsymbols(ar, x, y, n, m):
    symbols = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            nx = x + i
            ny = y + j
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if issymbol(ar, nx, ny):
                symbols.append((nx, ny))
    return symbols


def find(ar):
    n, m = len(ar), len(ar[0])
    for i in range(n):
        j = 0
        while j < m:
            if not ar[i][j].isdigit():
                j += 1
            else:
                cur = ''
                symbols = []
                while j < m and ar[i][j].isdigit():
                    symbols.extend(findsymbols(ar, i, j, n, m))
                    cur += ar[i][j]
                    j += 1
                for symbol in set(symbols):
                    symbolMap[symbol].append(int(cur))

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(line)

    find(ar)
    ans = 0
    for key, value in symbolMap.items():
        if len(value) == 2:
            ans += value[0] * value[1]

    return ans


for name in FILE_NAMES:
    symbolMap.clear()
    print(name, solve(name))
