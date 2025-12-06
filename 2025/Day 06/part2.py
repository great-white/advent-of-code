import os
from typing import List

FILE_NAMES = ['small', 'large']
YEAR = 2025
DAY = "Day 06"

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/{YEAR}/{DAY}/Input/{filename}.txt'
    ar: List[str] = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.replace('\n', '')
            ar.append(line)

    grand_ans: int = 0
    col_idx: int = 0

    def generate_eval_string() -> str:
        nonlocal col_idx
        operands: List[str] = []
        operation: str = ar[-1][col_idx] # we are sure to find an operation here

        # Iterate till we find a whole column of empty strings.
        while col_idx < len(ar[0]):
            # Iterate on all rows.
            break_point: bool = True
            operand: str = ''
            for row_idx in range(len(ar)):
                if ar[row_idx][col_idx] == ' ':
                    continue

                break_point = False
                if ar[row_idx][col_idx] in ('+', '*'):
                    continue
                operand += ar[row_idx][col_idx]
            
            col_idx += 1
            if break_point:
                return operation.join(operands)
            operands.append(operand)
        
        return operation.join(operands)

    while col_idx < len(ar[0]):
        eval_str: str = generate_eval_string()
        cur_ans: int = eval(eval_str)
        grand_ans += cur_ans
    
    return grand_ans

for name in FILE_NAMES:
    print(name, solve(name))
