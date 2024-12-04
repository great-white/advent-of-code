import os

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
    WORD = "XMAS"
    
    def horizontal(I, J):
        '''
        It will have 2 cases, forward and backward.
        '''
        nonlocal ar
        assert ar[I][J] == 'X'
        ans = 0

        # Going forward
        i, j = I, J
        k = 0
        while j < m and k < 4:
            if ar[i][j] != WORD[k]:
                break
            j += 1
            k += 1
        ans += k == 4

        # Going backward
        i, j = I, J
        k = 0
        while j >= 0 and k < 4:
            if ar[i][j] != WORD[k]:
                break
            j -= 1
            k += 1
        ans += k == 4

        return ans

    def vertical(I, J):
        '''
        It will have 2 cases, downward and upward.
        '''
        nonlocal ar
        assert ar[I][J] == 'X'
        ans = 0

        # Going downward
        i, j = I, J
        k = 0
        while i < n and k < 4:
            if ar[i][j] != WORD[k]:
                break
            i += 1
            k += 1
        ans += k == 4

        # Going upward
        i, j = I, J
        k = 0
        while i >= 0 and k < 4:
            if ar[i][j] != WORD[k]:
                break
            i -= 1
            k += 1
        ans += k == 4

        return ans

    def diagnol(I, J):
        '''
        It will have 4 cases, going in all 4 directions.
        '''
        nonlocal ar
        assert ar[I][J] == 'X'
        ans = 0

        # Going top-right
        i, j = I, J
        k = 0
        while i >= 0 and j < m and k < 4:
            if ar[i][j] != WORD[k]:
                break
            i -= 1
            j += 1
            k += 1
        ans += k == 4

        # Going bottom-right
        i, j = I, J
        k = 0
        while i < n and j < m and k < 4:
            if ar[i][j] != WORD[k]:
                break
            i += 1
            j += 1
            k += 1
        ans += k == 4

        # Going top-left
        i, j = I, J
        k = 0
        while i >= 0 and j >= 0 and k < 4:
            if ar[i][j] != WORD[k]:
                break
            i -= 1
            j -= 1
            k += 1
        ans += k == 4

        # Going bottom-left
        i, j = I, J
        k = 0
        while i < n and j >= 0 and k < 4:
            if ar[i][j] != WORD[k]:
                break
            i += 1
            j -= 1
            k += 1
        ans += k == 4

        return ans
    
    ans = 0
    for i in range(n):
        for j in range(m):
            if ar[i][j] == 'X':
                ans += horizontal(i, j) + vertical(i, j) + diagnol(i, j)
    
    return ans


for name in FILE_NAMES:
    print(name, solve(name))
