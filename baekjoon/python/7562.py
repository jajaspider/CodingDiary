from collections import deque
dx = [-1, -2, -2, -1, 1, 2, 1, 2]
dy = [2, 1, -1, -2, -2, -1, 2, 1]


def BFS(x,y,targetX,targetY):
    q = deque()
    q.append([x,y])
    visit[x][y] = 1
    while q:
        a,b = q.popleft()
        if a == targetX and b == targetY:
            print(int(visit[a][b]) - 1)
            return
        for i in range(0, 8):
            newX = a + dx[i]
            newY = b + dy[i]
            if 0 <= newX < int(I) and 0 <= newY < int(I) and int(visit[newX][newY]) == 0:
                q.append([newX, newY])
                visit[newX][newY] = visit[a][b] + 1

N = int(input())
for i in range(0, N):
    I = int(input())
    visit = [[0] * I for i in range(I)]
    x, y = map(int, input().split())
    targetX, targetY = map(int, input().split())
    BFS(x,y,targetX,targetY)

