import os

FILE_NAMES = ['small', 'large']
YEAR = 2024
DAY = "Day 02"

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(line)

    def isGood(cur):
        '''
        Determines if a given row is valid or not without any exception.
        '''
        valid = True
        isInc = cur[0] < cur[1]
        for idx in range(1, len(cur)):
            diff = abs(cur[idx] - cur[idx - 1])
            valid &= 1 <= diff <= 3
            valid &= isInc == (cur[idx - 1] < cur[idx])
        
        return valid
    
    def isGoodWithException(cur):
        '''
        Determines if a given row is valid after removing an element from it.
        '''
        for idx in range(len(cur)):
            _cur = cur[:]
            del _cur[idx]
            if isGood(_cur):
                return True
        
        return False

    ans = 0
    for row in ar:
        cur = list(map(int, row.split()))
        ans += isGood(cur) or isGoodWithException(cur)
    
    return ans

for name in FILE_NAMES:
    print(name, solve(name))
