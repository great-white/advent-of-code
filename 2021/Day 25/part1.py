from typing import List
from copy import deepcopy


YEAR = 2021
DAY = 'Day 25'
FILE_NAMES = ['small', 'large']


def moveEast(grid: List[List[str]]) -> List[List[str]]:
    indices = []
    n, m = len(grid), len(grid[0])

    # Find indices to move
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '>' and grid[i][(j + 1) % m] == '.':
                indices.append([i, j])

    # Actually move the indices
    for i, j in indices:
        grid[i][j] = '.'
        grid[i][(j + 1) % m] = '>'

    return grid


def moveSouth(grid: List[List[str]]) -> List[List[str]]:
    indices = []
    n, m = len(grid), len(grid[0])

    # Find indices to move
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'v' and grid[(i + 1) % n][j] == '.':
                indices.append([i, j])

    # Actually move the indices
    for i, j in indices:
        grid[i][j] = '.'
        grid[(i + 1) % n][j] = 'v'

    return grid


def performMove(grid: List[List[str]]) -> List[List[str]]:
    return moveSouth(moveEast(deepcopy(grid)))


def solve(filename):
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'
    grid = []

    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            grid.append(list(line))

    count = 1
    while True:
        newGrid = performMove(grid)
        if newGrid == grid:
            break
        grid = newGrid
        count += 1

    return count


for name in FILE_NAMES:
    print(name, solve(name))
