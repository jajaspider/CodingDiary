import sys

T = int(sys.stdin.readline())
for _ in range(0, T):
    hailstone = []
    n = int(sys.stdin.readline())
    hailstone.append(n)
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            hailstone.append(int(n))
        elif n % 2 == 1:
            n = n * 3 + 1
            hailstone.append(int(n))
    print(max(hailstone))

