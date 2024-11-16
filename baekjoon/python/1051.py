N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, list(input()))))

s = min(N, M)

for k in range(s, 0, -1):
    for i in range(0, N - k + 1):
        for j in range(0, M - k + 1):
            if matrix[i][j] == matrix[i + k - 1][j] == matrix[i][j + k - 1] == matrix[i + k - 1][j + k - 1]:
                print(k**2)
                exit()
