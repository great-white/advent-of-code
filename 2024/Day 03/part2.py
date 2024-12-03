import os
import re

FILE_NAMES = ['small2', 'large']
YEAR = 2024
DAY = "Day 03"

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(line)

    def extractDigitsAndProcess(item):
        a, b = map(int, item[4:-1].split(','))
        return a * b

    ans = 0
    enable = True
    for cur in ar:
        for match in re.finditer(r'(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don\'t\(\))', cur):
            matchStr = match.group()
            if matchStr.startswith('mul'):
                if enable:
                    ans += extractDigitsAndProcess(matchStr)
            elif matchStr.startswith('do()'):
                enable = True
            else:
                enable = False

    return ans

for name in FILE_NAMES:
    print(name, solve(name))
