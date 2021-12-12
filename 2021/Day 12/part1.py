from collections import defaultdict

YEAR = 2021
DAY = 'Day 12'
FILE_NAMES = ['small-01', 'small-02', 'small-03', 'large']


def solve(filename):
    graph = defaultdict(list)
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            a, b = line.strip().split('-')
            graph[a].append(b)
            graph[b].append(a)
        graph['end'] = []

    ans = 0
    queue = [['start']]

    while queue:
        root = queue.pop(0)
        cur = root[-1]
        if cur == 'end':
            ans += 1
            continue

        for node in graph[cur]:
            if node.islower() and node in root:
                continue
            temp = root + [node]
            queue.append(temp)

    return ans


for name in FILE_NAMES:
    print(name, solve(name))
