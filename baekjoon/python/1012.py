def DFS(x, y, count):
    visit[x][y] = 1

    for i in range(0, 4):
        newX = x + dx[i]
        newY = y + dy[i]

        if 0 <= newX < int(N) and 0 <= newY < int(N) and visit[newX][newY] == 0 and matrix[newX][newY] == 1:
            print(1)

            count += 1
            DFS(newX, newY, count)

    return count


T = int(input())
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
total = 0
for i in range(0, T):
    M, N, K = map(int, input().split())
    matrix = [[0] * M for j in range(N)]
    visit = [[0] * M for j in range(N)]
    print(matrix)
    for j in range(0, K):
        A, B = map(int, input().split())
        matrix[B][A] = 1

    for n in range(0, N):
        for m in range(0, M):
            if DFS(n, m, 0) > 0:
                total += 1

    print(total)
