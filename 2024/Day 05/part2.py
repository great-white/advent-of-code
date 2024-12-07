import os
from collections import defaultdict

FILE_NAMES = ['small', 'large']
YEAR = 2024
DAY = "Day 05"

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(line)

    d = defaultdict(list)
    for item in ar:
        if '|' in item:
            a, b = map(int, item.split('|'))
            d[a].append(b)
    
    def getExpectedUpdate(row):
        '''
        This helps in returning the expected order which needs to be 
        followed to satisfy the given constraints.
        '''
        inDegree = defaultdict(int)
        nodes = set()
        for key, values in d.items():
            if key not in row:
                continue
            nodes.add(key)
            for value in values:
                if value not in row:
                    continue
                inDegree[value] += 1
                nodes.add(value)
        
        queue = []
        for node in nodes:
            if inDegree[node] == 0:
                queue.append((node, 0))
        
        levels = dict()
        while queue:
            node, level = queue.pop(0)
            levels[node] = level
            for child in d[node]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    queue.append((child, level + 1))
        
        return [item[0] for item in sorted(levels.items(), key=lambda x: x[1])] 
    
    def process(row):
        '''
        Checks if the current update is correctly ordered.
        If yes, return the middle page.
        '''
        expectedRow = getExpectedUpdate(row)
        return expectedRow[len(expectedRow) // 2] if expectedRow != row else 0

    ans = 0
    for item in ar:
        if ',' in item:
            ans += process(list(map(int, item.split(','))))
            
    return ans    

for name in FILE_NAMES:
    print(name, solve(name))
