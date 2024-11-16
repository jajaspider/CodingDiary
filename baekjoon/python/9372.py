import sys

T = sys.stdin.readline().rstrip()
for i in range(0, int(T)):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    for j in range(0, int(M)):
        node1, node2 = map(int, sys.stdin.readline().rstrip().split())
    print(N - 1)
