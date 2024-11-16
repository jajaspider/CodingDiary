import sys

sys.setrecursionlimit(100000)

matrix = [[0] * 101 for i in range(101)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
N = 0
M = 0
count = 1


def bfs(x, y):
    queue = [[x, y]]
    visit = [[x, y]]
    distance = [[0 for _ in range(M+1)] for _ in range(N+1)]
    distance[0][0] = 1
    while queue:
        a, b = queue.pop(0)
        if a == N and b == M:
            break
        for i in range(4):
            newA = a + dx[i]
            newB = b + dy[i]
            if matrix[newA][newB] == "1" and [newA, newB] not in visit and 0 <= newA <= 100 and 0 <= newB <= 100:
                visit.append([newA, newB])
                queue.append([newA, newB])
                distance[newA][newB] = distance[a][b] + 1
    return distance[N][M]


def solution():
    global N, M, count
    N, M = map(int, input().split())
    for j in range(0, int(N)):
        tempstring = input()
        for i in range(0, int(M)):
            # 받아온데이터를 map배열에 입력
            matrix[j][i] = tempstring[i]

    N -= 1
    M -= 1
    print(bfs(0, 0))


solution()
