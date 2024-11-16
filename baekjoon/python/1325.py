from collections import deque


def dfs(start):
    q = deque()
    q.append(start)
    visit = [0 for _ in range(N + 1)]
    count = 1
    while q:
        now = q.popleft()
        visit[now] = 1
        if connect[now]:
            for nxt in connect[now]:
                if not visit[nxt]:
                    count += 1
                    visit[nxt] = 1
                    q.append(nxt)

    return count


N, M = map(int, input().split())
connect = [[] for i in range(0, N + 1)]
visit = []
countnum = [0 for i in range(0, N + 1)]

for _ in range(0, M):
    A, B = map(int, input().split())
    connect[B].append(A)

for i in range(1, N + 1):
    countnum[i] = dfs(i)

for i in range(1, N + 1):
    if max(countnum) == int(countnum[i]):
       print(i, end=" ")
