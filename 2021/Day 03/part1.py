YEAR = 2021
DAY = 'Day 03'
FILE_NAMES = ['small', 'large']


def solve(filename):
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(line)

    n = len(ar)
    m = len(ar[0])

    gamma, epsilon = '', ''

    for j in range(m):
        ones = zeros = 0
        for i in range(n):
            ones += ar[i][j] == '1'
            zeros += ar[i][j] == '0'
        if ones > zeros:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma * epsilon


for name in FILE_NAMES:
    print(name, solve(name))
