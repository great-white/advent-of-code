import os
from collections import defaultdict

FILE_NAMES = ['small', 'large']
YEAR = 2024
DAY = "Day 01"

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(line)
    
    left, right = [], []
    for item in ar:
        x, y = item.split()
        left.append(int(x))
        right.append(int(y))
    
    d = defaultdict(int)
    for key in right:
        d[key] += 1

    ans = 0

    for key in left:
        ans += key * d[key]
    
    return ans

for name in FILE_NAMES:
    print(name, solve(name))
