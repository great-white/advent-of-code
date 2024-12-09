import os
from collections import defaultdict
from itertools import combinations

FILE_NAMES = ['small', 'large']
YEAR = 2024
DAY = "Day 08"

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = list(line.strip())
            ar.append(line)
    n, m = len(ar), len(ar[0])
    d = defaultdict(list)
    
    for i in range(n):
        for j in range(m):
            if ar[i][j] != '.':
                d[ar[i][j]].append((i, j))
    
    def markAntinodesIfValid(x, y):
        nonlocal ar
        if 0 <= x < n and 0 <= y < m:
            ar[x][y] = '#'
    
    def findAntinodes(a, b):
        '''
        For each pair, only two antinodes are possible and those can be deduced 
        based on the slope of both the antennas's coordinates.
        '''
        
        # For first antinode. Taking a coordinate whose distance from 
        # `a` is equivalent to the distance between `a` and `b`.
        markAntinodesIfValid(2 * a[0] - b[0], 2 * a[1] - b[1])
        
        # For second antinode. Taking a coordinate whose distance from 
        # `b` is equivalent to the distance between `a` and `b`.
        markAntinodesIfValid(2 * b[0] - a[0], 2 * b[1] - a[1])
    
    for _ar in d.values():
        for a, b in combinations(_ar, 2):
            findAntinodes(a, b)
            
    return sum([row.count('#') for row in ar])
        
for name in FILE_NAMES:
    print(name, solve(name))
