visit = [0 for j in range(100001)]


def bfs(N, K):
    queue = [N]
    visit[N] = 1
    while queue:
        temp = queue.pop(0)
        if temp == K:
            return visit[temp] - 1
        for i in (temp - 1, temp + 1, 2 * temp):
            if 0 <= i < 100001 and visit[i] == 0:
                queue.append(i)
                visit[i] = visit[temp] + 1


def solution():
    N, K = map(int, input().split())
    print(bfs(N, K))


solution()
