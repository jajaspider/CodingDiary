T = int(input())
for i in range(0, T):
    n = int(input())
    room = [0 for _ in range(0, n)]
    for j in range(1, n+1):
        # j의 값에따라 배수의 방만
        a, b = divmod(n, j)
        for k in range(1, a+1):
            if room[j * k-1] == 0:
                room[j * k-1] = 1
            else:
                room[j * k-1] = 0

    roomcount = 0
    for j in range(0, n):
        if room[j] == 1:
            roomcount += 1
    print(roomcount)
