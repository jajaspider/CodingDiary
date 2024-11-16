import sys
sys.setrecursionlimit(100000)

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
count = 0


def DFS(x, y, N, M, matrix, visit):
    global count
    visit[x][y] = 1
    if int(matrix[x][y]) == 1:
        count += 1

    for i in range(0, 4):
        newX = x + dx[i]
        newY = y + dy[i]
        if 0 <= newX < int(N) and 0 <= newY < int(M) and int(visit[newX][newY]) == 0 and matrix[newX][newY] == 1:
            DFS(newX, newY, N, M, matrix, visit)


def solution():
    global count

    homecount = list()

    N, M, K = map(int, input().split())
    matrix = [[1] * M for i in range(N)]
    visit = [[0] * M for i in range(N)]
    for i in range(0, K):
        x1, y1, x2, y2 = map(int, input().split())
        for j in range(y1, y2):
            for k in range(x1, x2):
                matrix[j][k] = 0


    for j in range(0, int(N)):
        for i in range(0, int(M)):
            count = 0
            if not visit[j][i] and int(matrix[j][i]) != 0:
                DFS(j, i, N, M, matrix, visit)
                homecount.append(count)

    homecount.sort()
    print(len(homecount))
    for i in homecount:
        print(i, end=" ")


solution()
