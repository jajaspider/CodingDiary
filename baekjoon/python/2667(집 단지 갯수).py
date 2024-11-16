matrix = [[0] * 25 for i in range(25)]
visit = [[0] * 25 for i in range(25)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
N = 0
count = 0


def DFS(x, y):
    global count
    visit[x][y] = 1
    if matrix[x][y] == "1":
        count += 1

    for i in range(0, 4):
        newX = x + dx[i]
        newY = y + dy[i]

        if 0 <= newX < int(N) and 0 <= newY < int(N) and visit[newX][newY] == 0 and matrix[newX][newY] != "0":
            DFS(newX, newY)


def solution():
    global N, count

    homecount = list()
    N = input()
    for j in range(0, int(N)):
        tempstring = input()
        for i in range(0, int(N)):
            # 받아온데이터를 map배열에 입력
            matrix[j][i] = tempstring[i]

    for j in range(0, int(N)):
        for i in range(0, int(N)):
            count = 0
            if not visit[j][i] and matrix[j][i] != "0":
                DFS(j, i)
                homecount.append(count)

    homecount.sort()
    print(len(homecount))
    for i in homecount:
        print(i)


solution()
