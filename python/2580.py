sudoku = list()
zeros = list()
for _ in range(9):
    line = list(map(int, input().split()))
    sudoku.append(line)

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zeros.append([i, j])


def row(r, num):
    for i in range(9):
        if sudoku[r][i] == num:
            return False
    return True


def col(c, num):
    for i in range(9):
        if sudoku[i][c] == num:
            return False
    return True


def div(r, c, num):
    r //= 3
    c //= 3
    r *= 3
    c *= 3
    for i in range(r, r+3):
        for j in range(c, c+3):
            if sudoku[i][j] == num:
                return False
    return True


def sol_sudoku(depth):
    if depth == len(zeros):
        for i in range(9):
            print(*sudoku[i])
        exit(0)
    for i in range(1, 10):
        x, y = zeros[depth]

        if row(x, i) and col(y, i) and div(x, y, i):
            sudoku[x][y] = i
            sol_sudoku(depth+1)
            sudoku[x][y] = 0


sol_sudoku(0)
