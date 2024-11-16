import sys

sys.setrecursionlimit(100000)

matrix = [[0] * 250 for i in range(250)]
visit = [[0] * 250 for j in range(250)]
R = 0
C = 0
sheep = 0
wolf = 0
sheepcount = 0
wolfcount = 0
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def bfs(x, y):
    global sheepcount, wolfcount
    visit[x][y] = 1
    if matrix[x][y] == "o":
        sheepcount += 1
    elif matrix[x][y] == "v":
        wolfcount += 1

    for i in range(0, 4):
        newX = x + dx[i]
        newY = y + dy[i]

        if 0 <= newX < R and 0 <= newY < C and visit[newX][newY] == 0 and matrix[newX][newY] != "#":
            bfs(newX, newY)


def solution():
    # 처음 맵 크기를 입력받고
    global sheep, wolf, sheepcount, wolfcount, R, C
    R,C = map(int, input().split())
    # 세로만큼의 입력을 추가로 한줄씩 받아온다
    for j in range(0, int(R)):
        tempstring = input()
        for i in range(0, int(C)):
            # 받아온데이터를 map배열에 입력
            matrix[j][i] = tempstring[i]
    '''
    for j in range(0, int(R)):
        for i in range(0, int(C)):
            print(map[j][i], end="")
        print("")
    '''

    for j in range(0, int(R)):
        for i in range(0, int(C)):
            sheepcount = 0
            wolfcount = 0
            if not visit[j][i] and matrix[j][i] != "#":
                bfs(j, i)
                if sheepcount != 0 or wolfcount != 0:
                    if sheepcount > wolfcount:
                        sheep += sheepcount
                    else:
                        wolf += wolfcount

    print(str(sheep) + " " + str(wolf))


solution()
