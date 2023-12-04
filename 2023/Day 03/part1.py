import os
import re
from collections import defaultdict
from functools import reduce

FILE_NAMES = ['small', 'large']


def issymbol(ar, x, y):
    return not ar[x][y].isdigit() and not ar[x][y] == '.'


def hassymbol(ar, x, y, n, m):
    for i in range(-1, 2):
        for j in range(-1, 2):
            nx = x + i
            ny = y + j
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if issymbol(ar, nx, ny):
                return True
    return False


def find(ar):
    ans = 0
    n, m = len(ar), len(ar[0])
    for i in range(n):
        j = 0
        while j < m:
            if not ar[i][j].isdigit():
                j += 1
            else:
                cur = ''
                flag = False
                while j < m and ar[i][j].isdigit():
                    if hassymbol(ar, i, j, n, m):
                        flag = True
                    cur += ar[i][j]
                    j += 1
                if flag:
                    # print('cur', cur)
                    ans += int(cur)
    return ans

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(line)

    return find(ar)


for name in FILE_NAMES:
    print(name, solve(name))
