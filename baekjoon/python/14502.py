import copy
import sys

sys.setrecursionlimit(100000)

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
matrix = [[0] * 9 for _ in range(9)]
safezonecount = 0
virusList = []
N = 0
M = 0


def countsafe(tempmatrix):
    safezone = 0
    for j in range(0, int(N)):
        for i in range(0, int(M)):
            if tempmatrix[j][i] == 0:
                safezone += 1
    return safezone


def spreadvirus(x, y, tempmatrix):
    for i in range(0, 4):
        newX = x + dx[i]
        newY = y + dy[i]

        if 0 <= newX < N and 0 <= newY < M and tempmatrix[newX][newY] == 0:
            tempmatrix[newX][newY] = 2
            spreadvirus(newX, newY, tempmatrix)


def setwall(wallcount, start):
    global matrix, safezonecount

    if wallcount == 3:

        tempmatrix = copy.deepcopy(matrix)
        for i in range(0, len(virusList)):
            virusX, virusY = virusList[i]
            spreadvirus(virusX, virusY, tempmatrix)

        safezonecount = max(safezonecount, countsafe(tempmatrix))

        return

    for i in range(start, N * M):
        x = int(i / M)
        y = int(i % M)
        if matrix[x][y] == 0:
            matrix[x][y] = 1
            setwall(wallcount + 1, i + 1)
            matrix[x][y] = 0


def solution():
    global N, M, virusList
    N, M = map(int, input().split())
    global matrix

    for j in range(N):
        link = list(map(int, input().split()))
        for i in range(0, len(link)):
            matrix[j][i] = link[i]

    for j in range(0, int(N)):
        for i in range(0, int(M)):
            if matrix[j][i] == 2:
                virusList.append([j, i])

    setwall(0, 0)
    print(safezonecount)


solution()
