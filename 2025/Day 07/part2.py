import os
from typing import List

FILE_NAMES = ['small', 'large']
YEAR = 2025
DAY = "Day 07"

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/{YEAR}/{DAY}/Input/{filename}.txt'
    ar: List[List[str]] = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = list(line.strip())
            ar.append(line)

    # Get the position of 'S' in the first row.
    x, y = 0, ar[0].index('S')

    # Mark the starting point as 1.
    ar[x][y] = 1

    # Replace all '.' to 0.
    for row_idx in range(len(ar)):
        for col_idx in range(len(ar[0])):
            if ar[row_idx][col_idx] == '.':
                ar[row_idx][col_idx] = 0
    
    for row_idx in range(len(ar) - 1):
        for col_idx in range(len(ar[0])):
            # If current value is '^', ignore it.
            if ar[row_idx][col_idx] == '^':
                continue

            # Beam found, propogate it down.
            if ar[row_idx + 1][col_idx] == '^':
                # Splitter found, add current value to left and right of next row.
                ar[row_idx + 1][col_idx - 1] += ar[row_idx][col_idx]
                ar[row_idx + 1][col_idx + 1] += ar[row_idx][col_idx]
            else:
                # No splitter, just add value to the next row.
                ar[row_idx + 1][col_idx] += ar[row_idx][col_idx]

    return sum(ar[len(ar) - 1])

for name in FILE_NAMES:
    print(name, solve(name))
