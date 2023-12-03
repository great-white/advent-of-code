import os
import re
from collections import defaultdict
from functools import reduce

FILE_NAMES = ['small', 'large']


def find_powerset(game):
    dp = defaultdict(int)
    # print('game', game)
    sets = re.split(':|;', game)[1:]
    # print("sets", sets)
    for set in sets:
        items = set.strip().split(',')
        # print('items', items)
        for item in items:
            num, color = item.strip().split(' ')
            # print('num', num, color)
            dp[color] = max(int(num), dp[color])
    # print('dp', dp)
    return reduce((lambda x, y: x * y), dp.values())

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(line)

    ans = 0
    for i in range(len(ar)):
        ans += find_powerset(ar[i])
    
    return ans


for name in FILE_NAMES:
    print(name, solve(name))
