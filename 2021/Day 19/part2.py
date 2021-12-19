from typing import List, Set, Tuple


YEAR = 2021
DAY = 'Day 19'
FILE_NAMES = ['small', 'large']

finalBeacons: List[Set[Tuple[int, int, int]]] = []


def updateBeacons(idx: int,
                  curIdx: int,
                  relativePos: List[Tuple[int, int, int]]) -> Tuple[int, int, int]:
    global finalBeacons
    for x in range(-1, 2, 2):
        for y in range(-1, 2, 2):
            for z in range(-1, 2, 2):
                swapDp = [(0, 1, 2), (0, 2, 1), (1, 0, 2),
                          (1, 2, 0), (2, 0, 1), (2, 1, 0)]
                # Possibilities -> (x, y, z), (x, z, y), (y, x, z), (y, z, x), (z, x, y), (z, y, x)
                for swapX, swapY, swapZ in swapDp:
                    tempRelativePos = []
                    for relative in relativePos:
                        rx = relative[swapX] * x
                        ry = relative[swapY] * y
                        rz = relative[swapZ] * z
                        tempRelativePos.append((rx, ry, rz))

                    for (rx, ry, rz) in tempRelativePos:
                        for (bx, by, bz) in finalBeacons[idx]:
                            # Possible position for this scanner
                            sx, sy, sz = bx - rx, by - ry, bz - rz
                            curBeacons = set()
                            count = 0

                            # Checking if this is suitable position
                            # Atleast one pos should be there, else I'll be really sad.
                            for (rrx, rry, rrz) in tempRelativePos:
                                bbx, bby, bbz = rrx + sx, rry + sy, rrz + sz
                                curBeacons.add((bbx, bby, bbz))
                                count += (bbx, bby, bbz) in finalBeacons[idx]

                            if count >= 12:
                                # Finally, I found the scanner position
                                finalBeacons[curIdx] = curBeacons
                                return (sx, sy, sz)


def calculateManhattanDistance(a: Tuple[int, int, int], b: Tuple[int, int, int]) -> int:
    ans = 0
    for i in range(len(a)):
        ans += abs(a[i] - b[i])
    return ans


def solve(filename):
    global finalBeacons
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []

    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            if line == '':
                continue
            if line.startswith('---'):
                ar.append([])
                continue
            cur = list(map(int, line.split(',')))
            cur = tuple(cur)
            ar[-1].append(cur)

    finalBeacons = [set() for _ in range(len(ar))]
    for i in ar[0]:
        finalBeacons[0].add(i)
    scanners = [[] for _ in range(len(ar))]
    scanners[0] = (0, 0, 0)

    queue = [0]
    while queue:
        cur = queue.pop(0)
        for i in range(len(ar)):
            if finalBeacons[i]:
                continue
            scannerPos = updateBeacons(cur, i, ar[i])
            if scannerPos is None:
                continue
            scanners[i] = scannerPos
            queue.append(i)

    ans = 0
    for i in range(len(scanners)):
        for j in range(i + 1, len(scanners)):
            ans = max(ans, calculateManhattanDistance(
                scanners[i], scanners[j]))

    return ans


for name in FILE_NAMES:
    print(name, solve(name))
