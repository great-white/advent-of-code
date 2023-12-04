import os

FILE_NAMES = ['small', 'large']
YEAR = 2023
DAY = "Day 01"
SPELLED_DIGITS = {
    "one": "1", 
    "two": "2", 
    "three": "3", 
    "four": "4", 
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def find_first_digit(s):
    idx, val = 999, -1
    for key, value in SPELLED_DIGITS.items():
        cur = s.find(key)
        if cur != -1:
            if cur < idx:
                idx = cur
                val = value
    
    for key in range(10):
        cur = s.find(str(key))
        if cur != -1:
            if cur < idx:
                idx = cur
                val = str(key)
    
    return val


def find_last_digit(s):
    idx, val = -1, -1
    for key, value in SPELLED_DIGITS.items():
        cur = s.rfind(key)
        if cur != -1:
            if cur > idx:
                idx = cur
                val = value
    
    for key in range(10):
        cur = s.rfind(str(key))
        if cur != -1:
            if cur > idx:
                idx = cur
                val = str(key)
    
    return val

def solve(filename):
    INPUT_PATH = f'{os.path.expanduser("~")}/GitHub Projects/advent-of-code/{YEAR}/{DAY}/Input/{filename}.txt'
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
