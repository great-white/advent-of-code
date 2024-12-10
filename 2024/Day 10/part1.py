import os

FILE_NAMES = ['small', 'large']
YEAR = 2024
DAY = "Day 10"

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = list(map(int, list(line.strip())))
            ar.append(line)
    
    n, m = len(ar), len(ar[0])
    reach = [[set() for __ in range(m)] for _ in range(n)]
    
    X = [1, -1, 0, 0]
    Y = [0, 0, 1, -1]
    
    def dfs(x, y):
        if ar[x][y] == 9:
            reach[x][y] |= {(x, y)}
            return
        for i in range(4):
            nx = x + X[i]
            ny = y + Y[i]
            if 0 <= nx < n and 0 <= ny < m and ar[nx][ny] == ar[x][y] + 1:
                if not reach[nx][ny]:
                    dfs(nx, ny)
                reach[x][y] |= reach[nx][ny]
    
    ans = 0
    for i in range(n):
        for j in range(m):
            if ar[i][j] == 0:
                dfs(i, j)
                ans += len(reach[i][j])
    
    return ans
        
for name in FILE_NAMES:
    print(name, solve(name))
