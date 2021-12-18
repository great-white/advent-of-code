from math import ceil
from typing import List, Union

OK = 'OK'
NOT_OK = 'NOT_OK'
SPLIT = 'SPLIT'
EXPLODE = 'EXPLODE'


YEAR = 2021
DAY = 'Day 18'
FILE_NAMES = ['small', 'large']


class Pair:
    def __init__(self, a=None, b=None) -> None:
        self.a = a
        self.b = b

    def __str__(self) -> str:
        return f'[{self.a},{self.b}]'

    def __add__(self, other):
        return Pair(self, other)


def get_delimiter_index(a: str) -> int:
    count = 0
    for i in range(len(a)):
        if a[i] == '[':
            count += 1
        elif a[i] == ']':
            count -= 1

        if a[i] == ',' and count == 1:
            # Input is a pair
            return i

    # Input is a regular number
    return -1


def parse(a: str) -> Pair:
    start, end = 0, len(a) - 1
    idx = get_delimiter_index(a)

    if idx == -1:
        return int(a)

    first = a[start+1: idx]
    second = a[idx+1: end]

    return Pair(a=parse(first), b=parse(second))


def update_left(root: Pair, diff: int) -> None:
    while type(root.a) is not int:
        root = root.a
    root.a += diff


def update_right(root: Pair, diff: int) -> None:
    while type(root.b) is not int:
        root = root.b
    root.b += diff


def update_exact_right(root: Pair, diff: int) -> None:
    if type(root.b) is int:
        root.b += diff
        return
    update_left(root.b, diff)


def update_exact_left(root: Pair, diff: int) -> None:
    if type(root.a) is int:
        root.a += diff
        return
    update_right(root.a, diff)


def explode(root: Union[Pair, int], level: int = 1, stack: List[Pair] = []) -> str:
    if type(root) is int:
        return OK

    stack.append(root)

    cur = explode(root.a, level + 1, stack)
    if cur == EXPLODE:
        update_exact_right(root, root.a.b)

        # find parent that has a left child
        stack_size = len(stack)
        for i in range(stack_size - 2, -1, -1):
            if stack[i].a != stack[i + 1]:
                update_exact_left(stack[i], root.a.a)
                break

        root.a = 0
        return NOT_OK
    if cur == NOT_OK:
        return NOT_OK

    cur = explode(root.b, level + 1, stack)
    if cur == EXPLODE:
        update_exact_left(root, root.b.a)

        # find parent that has a right child
        stack_size = len(stack)
        for i in range(stack_size - 2, -1, -1):
            if stack[i].b != stack[i + 1]:
                update_exact_right(stack[i], root.b.b)
                break

        root.b = 0
        return NOT_OK
    if cur == NOT_OK:
        return NOT_OK

    if level > 4:
        return EXPLODE

    stack.pop()
    return OK


def split(root: Union[Pair, int]) -> str:
    if type(root) is int:
        if root >= 10:
            return SPLIT
        return OK

    cur = split(root.a)
    if cur == SPLIT:
        first = root.a // 2
        second = int(ceil(root.a / 2))
        root.a = Pair(first, second)
        return NOT_OK
    if cur == NOT_OK:
        return NOT_OK

    cur = split(root.b)
    if cur == SPLIT:
        first = root.b // 2
        second = int(ceil(root.b / 2))
        root.b = Pair(first, second)
        return NOT_OK
    if cur == NOT_OK:
        return NOT_OK

    return OK


def verify(root: Union[Pair, int]) -> str:
    while True:
        while explode(root) != OK:
            pass
        if split(root) == OK:
            break


def add(a: Pair, b: Pair) -> Pair:
    c = a + b
    verify(c)
    return c


def calculate_magnitude(a: Union[Pair, int]) -> int:
    if type(a) is int:
        return a

    return 3 * calculate_magnitude(a.a) + 2 * calculate_magnitude(a.b)


def solve(filename):
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []

    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(parse(line))

    ans = ar[0]
    for i in ar[1:]:
        ans = add(ans, i)

    return calculate_magnitude(ans)


for name in FILE_NAMES:
    print(name, solve(name))
