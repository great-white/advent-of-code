from typing import List
from copy import deepcopy


YEAR = 2021
DAY = 'Day 20'
FILE_NAMES = ['small', 'large']


def expand_image(image: List[List[str]], pad: str) -> List[List[str]]:
    n, m = len(image), len(image[0])
    img = [[pad] * (m + 4) for _ in range(n + 4)]

    for i in range(n):
        for j in range(m):
            img[i + 2][j + 2] = image[i][j]
    return img


def enhance_image(image: List[List[str]], algorithm: str, pad: str) -> List[List[str]]:
    image = expand_image(image, pad)
    new_image = deepcopy(image)
    final_image = []
    n, m = len(image), len(image[0])
    for i in range(1, n - 1):
        temp_row = []
        for j in range(1, m - 1):
            cur = ''
            for x in range(-1, 2):
                for y in range(-1, 2):
                    nx = i + x
                    ny = j + y
                    cur += '1' if image[nx][ny] == '#' else '0'
            idx = int(cur, 2)
            temp_row.append(algorithm[idx])
            new_image[i][j] = algorithm[idx]
        final_image.append(temp_row)

    return final_image


def count_light_pixel(image: List[List[str]]) -> int:
    ans = 0
    for row in image:
        ans += row.count('#')
    return ans


def solve(filename):
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'
    algorithm = ''
    image = []

    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            if not line:
                continue
            if not algorithm:
                algorithm = line
                continue
            image.append(list(line))

    pad = '.'
    TIMES = 2
    for i in range(TIMES):
        if filename == 'large':
            pad = '.' if i % 2 == 0 else '#'
        image = enhance_image(image, algorithm, pad)

    return count_light_pixel(image)


for name in FILE_NAMES:
    print(name, solve(name))
