import os

FILE_NAMES = ['small', 'large']


def find_first_digit(s):
    for i in s:
        if i.isdigit():
            return i

def find_last_digit(s):
    for i in s[::-1]:
        if i.isdigit():
            return i

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(line)

    ans = 0
    for word in ar:
        cur = find_first_digit(word) + find_last_digit(word)
        ans += int(cur)
    
    return ans


for name in FILE_NAMES:
    print(name, solve(name))
