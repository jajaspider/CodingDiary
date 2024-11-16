N = input()
A = list(map(int, input().split()))
B = sorted(A)

for i in range(0, len(A)):
    print(B.index(A[i]), end=" ")
    B[B.index(A[i])] = -1
# 3
# 2 3 1

# 1 2 0 P

# B[P[i]] = A[i]
# B[1] = 2
# B[2] = 3
# B[0] = 1
