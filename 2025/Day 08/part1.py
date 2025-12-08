import os
from typing import List, Set, Tuple, DefaultDict
from collections import defaultdict

FILE_NAMES = ['small', 'large']
YEAR = 2025
DAY = "Day 08"

class DisjoinUnionSet:
    def __init__(self, size):
        self.rank = [0] * size
        self.parent = list(range(size))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return
        
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[y_root] < self.rank[x_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/{YEAR}/{DAY}/Input/{filename}.txt'
    ar: List[List[int]] = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = list(map(int, line.strip().split(',')))
            ar.append(line)

    def calculate_distance(a: List[int], b: List[int]) -> float:
        # No need to take the square root, we just need relative values.
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2

    # Create a list for each pair with distance between them and sort them in ascending order.
    ordered_pairs: List[int] = []
    for i in range(len(ar)):
        for j in range(i + 1, len(ar)):
            distance = calculate_distance(ar[i], ar[j])
            ordered_pairs.append([i, j, distance])
    
    # Sort the pairs.
    ordered_pairs.sort(key=lambda x: -x[2])

    # We only need to connect with 1000 pairs if and only if they are not already connected.
    remaining_connections: int = 1000
    disjoint_set: DisjoinUnionSet = DisjoinUnionSet(len(ar))

    while ordered_pairs:
        if remaining_connections == 0:
            break

        a, b, _ = ordered_pairs.pop(-1)
        remaining_connections -= 1
        
        if disjoint_set.find(a) == disjoint_set.find(b):
            continue

        disjoint_set.union(a, b)

    # Now calculate the size of different circuits.
    unique_circuits: DefaultDict[int, int] = defaultdict(int)

    for i in range(len(ar)):
        parent = disjoint_set.find(i)
        unique_circuits[parent] += 1
    
    ans = sorted(unique_circuits.values(), reverse=True)
    
    if len(ans) < 3:
        return None

    return ans[0] * ans[1] * ans[2]

for name in FILE_NAMES:
    print(name, solve(name))
