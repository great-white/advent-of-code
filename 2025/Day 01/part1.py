import os

FILE_NAMES = ['small', 'large']
YEAR = 2025
DAY = "Day 01"

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(line)
    
    MOD = 100
    dial = 50
    ans = 0

    for cur in ar:
        direction, times = cur[0], int(cur[1:])
        if direction == 'R':
            dial += times
        else:
            dial -= times
        
        dial %= MOD
        ans += dial == 0
    
    return ans

for name in FILE_NAMES:
    print(name, solve(name))
