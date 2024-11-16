import sys

N = int(sys.stdin.readline())
Ns = []
for _ in range(0, N):
    Ns.append(float(sys.stdin.readline()))

Nmax = 0
for i in range(0, N):
    multi = 1
    for j in range(i, N):
        multi *= Ns[j]
        Nmax = multi if Nmax < multi else Nmax

print('%.3f' % Nmax)
