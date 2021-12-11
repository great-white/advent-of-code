YEAR = 2021
DAY = 'Day 04'
FILE_NAMES = ['small', 'large']


def solve(filename):
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'
    with open(INPUT_PATH, 'r') as f:
        ar = list(map(int, f.readline().split(',')))
        boards = []
        f.readline()  # Skip

        done = False
        while True:
            # Read a matrix
            mat = []
            for _ in range(5):
                cur = f.readline()
                if cur == '':
                    done = True
                    break
                temp = list(map(int, cur.split()))
                mat.append(temp)
            if done:
                break
            f.readline()
            boards.append(mat)

    def isRowDone(board, done):
        for row in board:
            count = 0
            for val in row:
                count += val in done
            if count == 5:
                return True
        return False

    def isColDone(board, done):
        temp = [[board[j][i] for j in range(5)] for i in range(5)]
        return isRowDone(temp, done)

    def calculateScore(board, done):
        ans = 0
        for row in board:
            for val in row:
                if val not in done:
                    ans += val
        return ans

    def getCountAndSum(board):
        done = set()
        count = 0
        for i in ar:
            count += 1
            done.add(i)
            if isRowDone(board, done) or isColDone(board, done):
                return count, calculateScore(board, done) * i
        return -1, -1

    globalCount, ans = 10 ** 9, 0
    for board in boards:
        count, score = getCountAndSum(board)
        if count == -1:
            continue
        if count < globalCount:
            globalCount = count
            ans = score

    return ans


for name in FILE_NAMES:
    print(name, solve(name))
