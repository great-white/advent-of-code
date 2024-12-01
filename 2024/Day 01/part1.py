import os

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
    
    left.sort()
    right.sort()

    ans = 0

    for x, y in zip(left, right):
        ans += abs(x - y)
    
    return ans

for name in FILE_NAMES:
    print(name, solve(name))
