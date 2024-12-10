import os

FILE_NAMES = ['small', 'large']
YEAR = 2024
DAY = "Day 09"

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(line)
    
    flag = True
    bid = 0
    
    s = []
    
    def updateFile(ch, times):
        nonlocal s
        s.extend([ch] * times)
    
    for ch in ar[0]:
        if flag:
            updateFile(str(bid), int(ch))
            bid += 1
        else:
            updateFile('.', int(ch))
        flag = not flag
        
    def getNextBlank(s, start):
        while start < len(s) and s[start] != '.':
            start += 1
        return start
        
    def process():
        nonlocal s
        start = getNextBlank(s, 0)
        while start < len(s) - 1:
            m = s.pop()
            s[start] = m
            start = getNextBlank(s, start)
    
    process()
    
    def checksum(s):
        ans = 0
        for idx, ch in enumerate(s):
            if ch == '.':
                continue
            ans += int(ch) * idx
        
        return ans
    
    return checksum(s)
        
for name in FILE_NAMES:
    print(name, solve(name))
