import os
from typing import List

FILE_NAMES = ['small', 'large']
YEAR = 2025
DAY = "Day 04"

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/{YEAR}/{DAY}/Input/{filename}.txt'
    ar: List[str] = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(line)

    n, m = len(ar), len(ar[0])
    ans = 0

    for i in range(n):
        for j in range(m):
            if ar[i][j] == '.':
                continue

            adjacent_rolls: int = 0

            # Calculate the number of adjacent rolls.
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    nx, ny = i + x, j + y
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    if ar[nx][ny] == '@':
                        adjacent_rolls += 1
            
            if adjacent_rolls < 4:
                ans += 1
    
    return ans


for name in FILE_NAMES:
    print(name, solve(name))
