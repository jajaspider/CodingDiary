import sys

T = int(sys.stdin.readline())
for i in range(0, T):
    N = int(sys.stdin.readline())
    xlist = []
    ylist = []
    for _ in range(0, N):
        x, y = map(float, sys.stdin.readline().split())
        xlist.append(x)
        ylist.append(y)
    sqaure = [min(xlist), max(xlist), min(ylist), max(ylist)]
    horizontal = abs(max(xlist) - min(xlist))
    vertical = abs(max(ylist) - min(ylist))
    sqaure_round = 2 * horizontal + 2 * vertical
    square_area = horizontal*vertical
    print("Case "+str(i+1)+": Area "+str(square_area)+", Perimeter "+str(sqaure_round))
