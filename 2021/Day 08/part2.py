YEAR = 2021
DAY = 'Day 08'
FILE_NAMES = ['small', 'large']


def solve(filename):
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'
    with open(INPUT_PATH, 'r') as _file:
        ans = 0
        for line in _file:
            d = dict()
            five, six = [], []
            cur = 0
            a, b = line.split(' | ')
            for i in a.split(' '):
                i = i.strip()
                if len(i) == 2:
                    d[1] = i
                elif len(i) == 4:
                    d[4] = i
                elif len(i) == 3:
                    d[7] = i
                elif len(i) == 7:
                    d[8] = i
                elif len(i) == 5:
                    five.append(i)
                else:
                    six.append(i)

            for i in five:
                if d[1][0] in i and d[1][1] in i:
                    d[3] = i
            for i in six:
                count = 0
                for j in d[3]:
                    count += j in i
                if count == 5:
                    d[9] = i

            five.remove(d[3])
            six.remove(d[9])

            for i in six:
                if d[1][0] in i and d[1][1] in i:
                    d[0] = i

            six.remove(d[0])

            for i in five:
                count = 0
                for j in i:
                    count += j in d[9]
                if count == 5:
                    d[5] = i

            five.remove(d[5])

            d[6] = six[0]
            d[2] = five[0]

            dd = dict()
            for key, value in d.items():
                dd[''.join(sorted(value))] = key

            cur = 0
            for i in b.split():
                i = i.strip()
                cur = 10 * cur + dd[''.join(sorted(i))]
            ans += cur

    return ans


for name in FILE_NAMES:
    print(name, solve(name))
