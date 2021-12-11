YEAR = 2021
DAY = 'Day 10'
FILE_NAMES = ['small', 'large']


def fun(s):
    stack = []
    for i in s.strip():
        if i in ['(', '[', '{', '<']:
            stack.append(i)
        else:
            if i == ')' and stack[-1] != '(':
                return []
            if i == ']' and stack[-1] != '[':
                return []
            if i == '>' and stack[-1] != '<':
                return []
            if i == '}' and stack[-1] != '{':
                return []
            stack.pop(-1)
    return stack


def solve(filename):
    d = {'(': 1, '[': 2, '{': 3, '<': 4}
    ans = []
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            stack = fun(line.strip())
            if not stack:
                continue
            cur = 0
            for i in stack[::-1]:
                cur *= 5
                cur += d[i]
            ans.append(cur)

    ans.sort()
    return ans[len(ans) // 2]


for name in FILE_NAMES:
    print(name, solve(name))
