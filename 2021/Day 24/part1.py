from functools import lru_cache


YEAR = 2021
DAY = 'Day 24'
FILE_NAMES = ['large']


instructions = []


def doFinalValidation(num: int) -> bool:
    num = list(str(num))
    w = x = y = z = 0
    d = {'x': x, 'y': y, 'z': z, 'w': w}

    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{FILE_NAMES[0]}.txt'
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip().split()

            if line[0] == 'inp':
                d['w'] = int(num.pop(0))
            else:
                op, a, b = line

                if op == 'add':
                    cur = f'{a}+{b}'
                elif op == 'mul':
                    cur = f'{a}*{b}'
                elif op == 'div':
                    cur = f'{a}//{b}'
                elif op == 'mod':
                    cur = f'{a}%{b}'
                else:
                    cur = f'{a}=={b}'
                try:
                    d[a] = eval(cur)
                except Exception as e:
                    print(cur, e)
                    return None

            w, x, y, z = d['w'], d['x'], d['y'], d['z']

    return d['z'] == 0


def isValid(idx: int, w: int, x: int, y: int, z: int) -> bool:
    assert 0 < w <= 9
    assert 0 <= idx < 14
    d = {'x': x, 'y': y, 'z': z, 'w': w}

    for op, a, b in instructions[idx]:
        cur = ''
        if op == 'add':
            cur = f'{a}+{b}'
        elif op == 'mul':
            cur = f'{a}*{b}'
        elif op == 'div':
            cur = f'{a}//{b}'
        elif op == 'mod':
            cur = f'{a}%{b}'
        else:
            cur = f'{a}=={b}'
        try:
            d[a] = eval(cur)
        except Exception as e:
            return None

        w, x, y, z = d['w'], d['x'], d['y'], d['z']

    return d['w'], d['x'], d['y'], d['z']


@lru_cache(None)
def fun(idx=0, x=0, y=0, z=0):
    if z > 10 ** 7:
        return None
    if idx == 14:
        if z != 0:
            return None
        return ''

    for num in range(9, 0, -1):
        cur = isValid(idx, num, x, y, z)
        if cur is None:
            continue
        nw, nx, ny, nz = cur
        rest = fun(idx + 1, nx, ny, nz)
        if rest is None:
            continue
        return str(num) + rest

    return None


def solve(filename):
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'

    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip().split()

            if line[0] == 'inp':
                instructions.append([])
            else:
                instructions[-1].append(line)

    return fun()


for name in FILE_NAMES:
    print(name, solve(name))
