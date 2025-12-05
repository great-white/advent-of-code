import os

FILE_NAMES = ['small', 'large']
YEAR = 2025
DAY = "Day 02"

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(line)
    
    def is_invalid(num):
        s_num = str(num)
        if len(s_num) % 2 != 0:
            return False

        half = len(s_num) // 2
        first, second = s_num[:half], s_num[half:]

        return first == second

    ans = 0

    for cur_range in ar[0].split(','):
        left, right = map(int, cur_range.split('-'))
        for num in range(left, right + 1):
            if is_invalid(num):
                ans += num
    
    return ans


for name in FILE_NAMES:
    print(name, solve(name))
