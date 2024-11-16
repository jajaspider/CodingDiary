import sys

N, L = map(int, sys.stdin.readline().split())
M = list(map(int, sys.stdin.readline().split()))
M.sort()

s = 0
cnt = 0
for tape in M:
    if s < tape:
        s = tape + L - 1
        cnt += 1
print(cnt)