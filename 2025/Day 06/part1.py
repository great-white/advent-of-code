import os
from typing import List

FILE_NAMES = ['small', 'large']
YEAR = 2025
DAY = "Day 06"

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/{YEAR}/{DAY}/Input/{filename}.txt'
    ar: List[List[str]] = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip().split()
            ar.append(line)

    grand_ans: int = 0

    for j in range(len(ar[0])):
        operation: str = ar[-1][j]
        operands: List[str] = []
        for i in range(len(ar) - 1):
            operands.append(ar[i][j])
        
        eval_str: str = operation.join(operands)
        cur_ans: int = eval(eval_str)
        grand_ans += cur_ans
    
    return grand_ans

for name in FILE_NAMES:
    print(name, solve(name))
