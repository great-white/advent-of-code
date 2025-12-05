import os
from typing import List

FILE_NAMES = ['small', 'large']
YEAR = 2025
DAY = "Day 05"

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/{YEAR}/{DAY}/Input/{filename}.txt'
    ar: List[str] = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(line)

    fresh_ingredients: List[range] = []

    flag = True
    ans = 0
    for line in ar:
        if not line:
            flag = False
            continue

        if flag:
            start, end = map(int, line.split('-'))
            fresh_ingredients.append(range(start, end + 1))
        else:
            ingredient = int(line)
            
            for fresh_ingredient_range in fresh_ingredients:
                if ingredient in fresh_ingredient_range:
                    ans += 1
                    break
    
    return ans


for name in FILE_NAMES:
    print(name, solve(name))
