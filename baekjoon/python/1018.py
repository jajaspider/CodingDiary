def start_point(A, B):
    count1, count2 = 0, 0
    for y in range(A, A + 8):
        for x in range(B, B + 8):
            if (x + y) % 2 == 0:
                if matrix[x][y] == 'B':
                    count1 += 1
            else:
                if matrix[x][y] == 'W':
                    count1 += 1

    for y in range(A, A + 8):
        for x in range(B, B + 8):
            if (x + y) % 2 == 0:
                if matrix[x][y] == 'W':
                    count2 += 1
            else:
                if matrix[x][y] == 'B':
                    count2 += 1
    min_list.append(count1)
    min_list.append(count2)

min_list = []
R, C = map(int, input().split())
# 세로만큼의 입력을 추가로 한줄씩 받아온다
matrix = [[0] * C for i in range(R)]
for j in range(0, int(R)):
    tempstring = input()
    for i in range(0, int(C)):
        # 받아온데이터를 map배열에 입력
        matrix[j][i] = tempstring[i]

for j in range(0, R - 7):
    for i in range(0, C - 7):
        start_point(i, j)

print(min(min_list))