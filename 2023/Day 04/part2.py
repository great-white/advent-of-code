import os
import re
from collections import defaultdict
from functools import reduce

YEAR = 2023
DAY = "Day 04"
FILE_NAMES = ['small', 'large']
countMap = defaultdict(int)

def findnums(row):
    items = re.split(r':|\|', row)[1:]
    items = [set(item.strip().split()) for item in items]
    # print('set', items)
    return items[0] & items[1]
    

def updatecountmap(start, next_cards, times):
    while next_cards > 0:
        next_cards -= 1
        countMap[start] += times
        start += 1

def solve(filename):
    INPUT_PATH = f'{os.path.expanduser("~")}/GitHub Projects/advent-of-code/{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(line)

    ans = 0
    cardnum = 1
    for row in ar:
        countMap[cardnum] += 1
        nums = findnums(row)
        # print('nums', nums)
        updatecountmap(cardnum + 1, len(nums), countMap[cardnum])
        cardnum += 1

    # print('countmap', countMap)
    return sum(countMap.values())


for name in FILE_NAMES:
    countMap.clear()
    print(name, solve(name))
