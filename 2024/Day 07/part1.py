import os

FILE_NAMES = ['small', 'large']
YEAR = 2024
DAY = "Day 07"

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(line)

    def dfs(lhs, rhs, idx, cur):
        if idx == len(rhs):
            return lhs == cur
        return dfs(lhs, rhs, idx + 1, cur + rhs[idx]) or dfs(lhs, rhs, idx + 1, cur * rhs[idx])

    def process(equation):
        lhs, rhs = equation.split(':')
        lhs = int(lhs.strip())
        rhs = list(map(int, rhs.strip().split()))
        
        return lhs if dfs(lhs, rhs, 1, rhs[0]) else 0
    
    return sum([process(equation) for equation in ar])
        
for name in FILE_NAMES:
    print(name, solve(name))
