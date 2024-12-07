import os

FILE_NAMES = ['small', 'large']
YEAR = 2024
DAY = "Day 06"

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = list(line.strip())
            ar.append(line)

    x = y = -1
    n, m = len(ar), len(ar[0])
    
    # Figure out the starting position of the guard.
    for i in range(n):
        for j in range(m):
            if ar[i][j] == '^':
                x, y = i, j
                break

    inc = (-1, 0)
    
    def turnRight():
        if inc == (-1, 0):
            return (0, 1)
        if inc == (0, 1):
            return (1, 0)
        if inc == (1, 0):
            return (0, -1)
        return (-1, 0)
    
    while True:
        total += 1
        ar[x][y] = 'X'
        nx, ny = x + inc[0], y + inc[1]
        if not(0 <= nx < n and 0 <= ny < m):
            break
        if ar[nx][ny] == '#':
            inc = turnRight()
            continue
        x, y = nx, ny
       
    return sum([row.count('X') for row in ar])
        
for name in FILE_NAMES:
    print(name, solve(name))
