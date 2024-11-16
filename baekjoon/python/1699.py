N = int(input())
Nlist = [0] * (N + 1)
for i in range(1, N + 1):
    Nlist[i] = i
    for j in range(1, i):
        if (j * j) > i:
            break
        if Nlist[i] > Nlist[i - j * j] + 1:
            Nlist[i] = Nlist[i - j * j] + 1
print(Nlist[N])
