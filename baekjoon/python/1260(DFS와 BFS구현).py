def dfs(current, matrix, visit=None):
    if visit is None:
        visit = list()
    visit.append(current)
    for i in range(len(matrix[current])):
        if matrix[current][i] == 1 and i not in visit:
            visit = dfs(i, matrix, visit)
    return visit


def bfs(current, matrix):
    queue = [current]
    visit = [current]
    while queue:
        current_node = queue.pop(0)
        for i in range(len(matrix[current_node])):
            if matrix[current_node][i] == 1 and i not in visit:
                visit.append(i)
                queue.append(i)
    return visit


def solution():
    N, M, V = map(int, input().split())
    matrix = [[0] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        link = list(map(int, input().split()))
        matrix[link[0]][link[1]] = 1
        matrix[link[1]][link[0]] = 1

    print(*dfs(V, matrix))
    print(*bfs(V, matrix))


solution()
