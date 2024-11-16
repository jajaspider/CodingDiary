def rec(n, a, b, c):
    if n == 1:
        move.append([a, c])
    else:
        rec(n-1,a,c,b)
        move.append(([a,c]))
        rec(n-1,b,a,c)


move = []
N = int(input())
rec(N, 1, 2, 3)
print(len(move))
for i in move:
    print(str(i[0])+' '+str(i[1]))