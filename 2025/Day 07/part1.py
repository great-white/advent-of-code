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

    # Put the starting point in the queue.
    queue = [(x, y)]

    # Initialize the ans.
    ans = 0

    while queue:
        x, y = queue.pop(0) # pop the first element.

        # Check if next row is there or not.
        if x + 1 >= len(ar):
            continue

        # Check the next row.
        if ar[x + 1][y] == '^':
            ans += 1
            # Found splitter, split the beam. Keep in mind about the bounds of y.
            if y - 1 >= 0 and ar[x + 1][y - 1] == '.':
                ar[x + 1][y - 1] = '|'
                queue.append((x + 1, y - 1))
            if y + 1 < len(ar[0]) and ar[x + 1][y + 1] == '.':
                ar[x + 1][y + 1] = '|'
                queue.append((x + 1, y + 1))
        else:
            # No splitter.
            if ar[x + 1][y] == '.':
                ar[x + 1][y] = '|'
                queue.append((x + 1, y))

    return ans

for name in FILE_NAMES:
    print(name, solve(name))
