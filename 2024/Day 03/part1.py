import os
import re

FILE_NAMES = ['small', 'large']
YEAR = 2024
DAY = "Day 03"

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(line)
    
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    
    def extractDigitsAndProcess(item):
        a, b = map(int, item[4:-1].split(','))
        return a * b

    ans = 0
    for cur in ar:
        ans += sum([extractDigitsAndProcess(item) for item in re.findall(pattern, cur)])

    return ans

for name in FILE_NAMES:
    print(name, solve(name))
