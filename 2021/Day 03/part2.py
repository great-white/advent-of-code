YEAR = 2021
DAY = 'Day 03'
FILE_NAMES = ['small', 'large']


def getMaxNums(ar, tpe, bit):
    n = len(ar)
    ones, zeros = [], []
    for i in range(n):
        if ar[i][bit] == '1':
            ones.append(ar[i])
        else:
            zeros.append(ar[i])

    if tpe == 'o2':
        ar = zeros if len(zeros) > len(ones) else ones
    else:
        ar = ones if len(ones) < len(zeros) else zeros
    return ar


def getO2(ar):
    m = len(ar[0])
    for i in range(m):
        ar = getMaxNums(ar, 'o2', i)
        if len(ar) == 1:
            break
    return ar[0]


def getCO2(ar):
    m = len(ar[0])
    for i in range(m):
        ar = getMaxNums(ar, 'co2', i)
        if len(ar) == 1:
            break
    return ar[0]


def solve(filename):
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(line)

    n = len(ar)
    m = len(ar[0])

    o2 = getO2(ar)
    co2 = getCO2(ar)

    o2 = int(o2, 2)
    co2 = int(co2, 2)
    return o2 * co2


for name in FILE_NAMES:
    print(name, solve(name))
