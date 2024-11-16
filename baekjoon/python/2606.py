import sys


def dfs(start=1):
    visit[start] = 1
    for i in range(1, len(matrix[start])):
        if matrix[start][i] == 1 and visit[i] == 0:
            # print("dfs",start,i)
            dfs(i)


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

matrix = [[0] * (N + 1) for i in range(0, N + 1)]
visit = [0 for i in range(0, N + 1)]

for i in range(0, M):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

dfs()
cnt = 0
for i in range(2, len(visit)):
    if visit[i] == 1:
        cnt += 1

print(cnt)
