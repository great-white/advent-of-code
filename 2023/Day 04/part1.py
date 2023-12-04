import os
import re
from collections import defaultdict
from functools import reduce

FILE_NAMES = ['small', 'large']
YEAR = 2023
DAY = "Day 04"

def findnums(row):
    items = re.split(r':|\|', row)[1:]
    items = [set(item.strip().split()) for item in items]
    # print('set', items)
    return items[0] & items[1]
    

def solve(filename):
    INPUT_PATH = f'{os.path.expanduser("~")}/GitHub Projects/advent-of-code/{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(line)

    ans = 0
    for row in ar:
        nums = findnums(row)
        # print('nums', nums)
        if len(nums) == 0:
            continue
        ans += pow(2, len(nums) - 1)
    return ans


for name in FILE_NAMES:
    print(name, solve(name))
