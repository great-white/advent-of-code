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
    
    def labelPages():
        '''
        This helps in labelling the nodes. Each label is a level at which current page 
        should be printed to maintain the correct order.
        '''
        inDegree = defaultdict(int)
        nodes = set()
        for key, values in d.items():
            nodes.add(key)
            for value in values:
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
        
        return levels

    labels = labelPages() 
    
    def process(row):
        '''
        Checks if the current update is correctly ordered.
        If yes, return the middle page.
        '''
        level = -1
        for node in row:
            curLevel = labels[node]
            if curLevel < level:
                return 0
            level = curLevel
        
        return row[len(row) // 2]

    ans = 0
    for item in ar:
        if ',' in item:
            ans += process(list(map(int, item.split(','))))
            
    return ans    

for name in FILE_NAMES:
    print(name, solve(name))
