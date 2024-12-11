import os
import time

FILE_NAMES = ['small', 'large']
YEAR = 2024
DAY = "Day 11"

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = list(map(int, line.strip().split()))
            ar.append(line)
    
    memo = dict()
    
    def dfs(num, steps=0):
        if (num, steps) in memo:
            return memo[(num, steps)]
        if steps == 75:
            memo[(num, steps)] = 1
            return 1
        if num == 0:
            memo[(num, steps)] = dfs(num + 1, steps + 1)
            return memo[(num, steps)]
        if len(str(num)) % 2 == 0:
            mid = len(str(num)) // 2
            memo[(num, steps)] = dfs(int(str(num)[:mid]), steps + 1) + dfs(int(str(num)[mid:]), steps + 1)
            return memo[(num, steps)]
        memo[(num, steps)] = dfs(num * 2024, steps + 1)
        return memo[(num, steps)]
    
    return sum([dfs(num) for num in ar[0]])
        
for name in FILE_NAMES:
    # Start time
    begin = time.time()
    # Actual execution
    ans = solve(name)
    # End time
    end = time.time()
    # Output
    print(name, solve(name), '\tTime', end - begin)
