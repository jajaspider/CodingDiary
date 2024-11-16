import sys
sys.setrecursionlimit(100000)

'''
0 2 3 4 5 6 7 8 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
2 4 5 0 0 0 0 0 0
0 6 7 0 0 0 0 0 0
3 8 9 0 0 0 0 0 0
'''

sudoku = [list(map(int, input().split())) for _ in range(9)]

zero_list = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]


def requirement(x, y):
    sudoku_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(0, 9):
        if sudoku[x][i] in sudoku_list:
            sudoku_list.remove(sudoku[x][i])
        if sudoku[i][y] in sudoku_list:
            sudoku_list.remove(sudoku[i][y])

    x = x // 3
    y = y // 3
    for i in range(x * 3, (x + 1) * 3):
        for j in range(y * 3, (y + 1) * 3):
            if sudoku[i][j] in sudoku_list:
                sudoku_list.remove(sudoku[i][j])

    return sudoku_list


def dfs(num):
    global complete
    if complete == 1:
        return

    if num == len(zero_list):
        for row in sudoku:
            print(*row)
        complete = 1
        return
    else:
        x, y = zero_list[num]
        req = requirement(x, y)

        for i in req:
            sudoku[x][y] = i
            dfs(num + 1)
            sudoku[x][y] = 0


complete = 0
dfs(0)
