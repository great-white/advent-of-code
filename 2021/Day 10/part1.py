from collections import defaultdict
YEAR = 2021
DAY = 'Day 10'
FILE_NAMES = ['small', 'large']


def fun(s):
    stack = []
    for i in s:
        if i in ['(', '[', '{', '<']:
            stack.append(i)
        else:
            if i == ')' and stack[-1] != '(':
                return ')'
            if i == ']' and stack[-1] != '[':
                return ']'
            if i == '>' and stack[-1] != '<':
                return '>'
            if i == '}' and stack[-1] != '{':
                return '}'
            stack.pop()
    return ''


def solve(filename):
    d = defaultdict(int)
    ans = 0
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            cur = fun(line)
            d[cur] += 1

    ans += d[')'] * 3
    ans += d[']'] * 57
    ans += d['}'] * 1197
    ans += d['>'] * 25137

    return ans


for name in FILE_NAMES:
    print(name, solve(name))
