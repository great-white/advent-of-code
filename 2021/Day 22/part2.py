from typing import List, Tuple
from parse import parse
from itertools import product


YEAR = 2021
DAY = 'Day 22'
FILE_NAMES = ['part-02-small', 'large']


def doesOverlap(cube1: List[Tuple[int, int]], cube2: List[Tuple[int, int]]) -> bool:
    xOverlap = cube1[0][0] > cube2[0][1] or cube1[0][1] < cube2[0][0]
    yOverlap = cube1[1][0] > cube2[1][1] or cube1[1][1] < cube2[1][0]
    zOverlap = cube1[2][0] > cube2[2][1] or cube1[2][1] < cube2[2][0]

    ans = xOverlap or yOverlap or zOverlap
    return not ans


def isValid(cube: List[Tuple[int, int]]) -> bool:
    return cube[0][0] <= cube[0][1] and cube[1][0] <= cube[1][1] and cube[2][0] <= cube[2][1]


def divide(oldCube: List[Tuple[int, int]], newCube: List[Tuple[int, int]]) -> List[List[Tuple[int, int]]]:
    ans = []
    x = [(oldCube[0][0], newCube[0][0] - 1), (newCube[0][1] + 1, oldCube[0][1]),
         (max(oldCube[0][0], newCube[0][0]), min(oldCube[0][1], newCube[0][1]))]
    y = [(oldCube[1][0], newCube[1][0] - 1), (newCube[1][1] + 1, oldCube[1][1]),
         (max(oldCube[1][0], newCube[1][0]), min(oldCube[1][1], newCube[1][1]))]
    z = [(oldCube[2][0], newCube[2][0] - 1), (newCube[2][1] + 1, oldCube[2][1]),
         (max(oldCube[2][0], newCube[2][0]), min(oldCube[2][1], newCube[2][1]))]

    for cur in product(x, y, z):
        if cur == (x[2], y[2], z[2]):
            continue
        cur = list(cur)
        if isValid(cur) and not doesOverlap(cur, newCube):
            ans.append(cur)

    return ans


def countCubes(cubes: List[List[Tuple[int, int]]]) -> int:
    ans: int = 0
    for x, y, z in cubes:
        ans += (x[1] - x[0] + 1) * (y[1] - y[0] + 1) * (z[1] - z[0] + 1)
    return ans


def mitigateOverlap(cubes: List[List[Tuple[int, int]]], newCube: List[Tuple[int, int]]) -> List[List[Tuple[int, int]]]:
    ans: List[List[Tuple[int, int]]] = []
    for oldCube in cubes:
        if doesOverlap(oldCube, newCube):
            ans.extend(divide(oldCube, newCube))
        else:
            ans.append(oldCube)
    return ans


def solve(filename):
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'
    cubes: List[List[Tuple[int, int]]] = []

    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            d = parse('{action} x={sx}..{ex},y={sy}..{ey},z={sz}..{ez}', line)
            d = d.named

            for key in d.keys():
                if key == 'action':
                    continue
                d[key] = int(d[key])

            newCube = [(d['sx'], d['ex']), (d['sy'], d['ey']),
                       (d['sz'], d['ez'])]
            cubes = mitigateOverlap(cubes, newCube)
            if d['action'] == 'on':
                cubes.append(newCube)

    return countCubes(cubes)


for name in FILE_NAMES:
    print(name, solve(name))
