import os

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
    
    def processOnce(ar):
        _ar = []
        while ar:
            cur = ar.pop(0)
            if cur == 0:
                cur += 1
            elif len(str(cur)) % 2 == 0:
                size = len(str(cur))
                mid = size // 2
                _ar.append(int(str(cur)[:mid]))
                cur = int(str(cur)[mid:])
            else:
                cur *= 2024
            _ar.append(cur)
        return _ar
    
    ar = ar[0]
    for i in range(25):
        ar = processOnce(ar)
    
    return len(ar)
        
for name in FILE_NAMES:
    print(name, solve(name))
