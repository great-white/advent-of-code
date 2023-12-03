import os
import re

FILE_NAMES = ['small', 'large']
VALID = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def is_valid_game(game):
    # print('game', game)
    sets = re.split(':|;', game)[1:]
    # print("sets", sets)
    for set in sets:
        items = set.strip().split(',')
        # print('items', items)
        for item in items:
            num, color = item.strip().split(' ')
            # print('num', num, color)
            if int(num) > VALID[color]:
                return False
    return True

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(line)

    ans = 0
    for i in range(len(ar)):
        if is_valid_game(ar[i]):
            ans += i + 1
    
    return ans


for name in FILE_NAMES:
    print(name, solve(name))
