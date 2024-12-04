import os
import re

FILE_NAMES = ['small', 'large']
YEAR = 2024
DAY = "Day 04"

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(line)

    n, m = len(ar), len(ar[0])
    WORD = "MAS"
    
    def findMas(I, J):
        '''
        It will have 4 cases. Reading strings from top-left to bottom-right and top-right to bottom-left.
        1. MAS - MAS
        2. MAS - SAM
        3. SAM - MAS
        4. SAM - SAM
        '''
        nonlocal ar
        assert ar[I][J] == 'A'
        ans = 0

        A = [(-1, -1), (0, 0), (1, 1)]
        B = [(-1, 1), (0, 0), (1, -1)]

        # Checking for first case.
        k1, k2 = 0, 0
        for x in range(3):
            nx1 = I + A[x][0]
            ny1 = J + A[x][1]
            nx2 = I + B[x][0]
            ny2 = J + B[x][1]
            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m and k1 < 3 and k2 < 3:
                if ar[nx1][ny1] != WORD[k1] or ar[nx2][ny2] != WORD[k2]:
                    break
                k1 += 1
                k2 += 1
        ans += k1 == 3 and k2 == 3

        # Checking for second case.
        k1, k2 = 0, 2
        for x in range(3):
            nx1 = I + A[x][0]
            ny1 = J + A[x][1]
            nx2 = I + B[x][0]
            ny2 = J + B[x][1]
            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m and k1 < 3 and k2 >= 0:
                if ar[nx1][ny1] != WORD[k1] or ar[nx2][ny2] != WORD[k2]:
                    break
                k1 += 1
                k2 -= 1
        ans += k1 == 3 and k2 == -1

        # Checking for third case.
        k1, k2 = 2, 0
        for x in range(3):
            nx1 = I + A[x][0]
            ny1 = J + A[x][1]
            nx2 = I + B[x][0]
            ny2 = J + B[x][1]
            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m and k1 >= 0 and k2 < 3:
                if ar[nx1][ny1] != WORD[k1] or ar[nx2][ny2] != WORD[k2]:
                    break
                k1 -= 1
                k2 += 1
        ans += k1 == -1 and k2 == 3

        # Checking for fourth case.
        k1, k2 = 2, 2
        for x in range(3):
            nx1 = I + A[x][0]
            ny1 = J + A[x][1]
            nx2 = I + B[x][0]
            ny2 = J + B[x][1]
            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m and k1 >= 0 and k2 >= 0:
                if ar[nx1][ny1] != WORD[k1] or ar[nx2][ny2] != WORD[k2]:
                    break
                k1 -= 1
                k2 -= 1
        ans += k1 == -1 and k2 == -1

        return ans
    
    ans = 0
    for i in range(n):
        for j in range(m):
            if ar[i][j] == 'A':
                ans += findMas(i, j)
    
    return ans


for name in FILE_NAMES:
    print(name, solve(name))
