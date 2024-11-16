matrix = [[0] * 101 for i in range(101)]
colormatrix = [[0] * 101 for i in range(101)]
visit = [[0] * 101 for i in range(101)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
N = 0


def DFS(x, y, alpha):
    global visit
    visit[x][y] = 1
    for i in range(0, 4):
        newX = x + dx[i]
        newY = y + dy[i]
        if 0 <= newX < int(N) and 0 <= newY < int(N) and visit[newX][newY] == 0 and matrix[newX][newY] == alpha:
            DFS(newX, newY, alpha)


def solution():
    global matrix, visit, N

    count = 0
    N = input()
    for j in range(0, int(N)):
        tempstring = input()
        for i in range(0, int(N)):
            # 받아온데이터를 map배열에 입력
            matrix[j][i] = tempstring[i]

    for j in range(0, int(N)):
        for i in range(0, int(N)):
            if matrix[j][i] == "R" and visit[j][i] == 0:
                DFS(j, i, "R")
                count += 1
            if matrix[j][i] == "G" and visit[j][i] == 0:
                DFS(j, i, "G")
                count += 1
            if matrix[j][i] == "B" and visit[j][i] == 0:
                DFS(j, i, "B")
                count += 1

    print(count,end=" ")
    for j in range(0, int(N)):
        for i in range(0, int(N)):
            if matrix[j][i] == "G":
                matrix[j][i] = "R"

    for j in range(0, int(N)):
        for i in range(0, int(N)):
            visit[j][i] = 0

    count = 0
    for j in range(0, int(N)):
        for i in range(0, int(N)):
            if matrix[j][i] == "R" and visit[j][i] != 1:
                DFS(j, i, "R")
                count += 1
            if matrix[j][i] == "B" and visit[j][i] != 1:
                DFS(j, i, "B")
                count += 1
    print(count)



solution()
