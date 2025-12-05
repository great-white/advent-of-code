import os

FILE_NAMES = ['small', 'large']
YEAR = 2025
DAY = "Day 03"

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(line)

    ans = 0

    for line in ar:
        first_max = max(line)
        first_max_idx = line.find(first_max)
        
        if first_max_idx == len(line) - 1:
            pre_first_max = max(line[:-1])
            cur_max = pre_first_max + first_max
        else:
            second_max = max(line[first_max_idx+1:])
            cur_max = first_max + second_max
        
        ans += int(cur_max)
    
    return ans

for name in FILE_NAMES:
    print(name, solve(name))
