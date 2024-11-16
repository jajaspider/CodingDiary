import sys

sys.setrecursionlimit(10000)


def dfs(a):
    visit[a] = 1
    for j in matrix[a]:
        if visit[j] != 1:
            dfs(j)


N, M = map(int, sys.stdin.readline().split())
matrix = [[] for _ in range(N+1)]
visit = [0] * (N+1)
count = 0

for i in range(0, M):
    u, v = map(int, sys.stdin.readline().split())
    matrix[u].append(v)
    matrix[v].append(u)

for i in range(0, N):
    if visit[i] != 1:
        dfs(i)
        count += 1

print(count)
