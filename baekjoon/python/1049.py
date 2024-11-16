# 조건 추가
import sys

N, M = map(int, sys.stdin.readline().split())
six = 1001
one = 1001
for _ in range(0, M):
    A, B = map(int, sys.stdin.readline().split())
    six = six if six < A else A
    one = one if one < B else B

if N > 6:
    x = N // 6
    y = N % 6
    price = [(x + 1) * six, x * six + y * one, N*one]
    print(min(price))
else:
    print(six if six < N * one else N * one)
