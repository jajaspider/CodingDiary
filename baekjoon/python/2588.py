A = int(input())
B = int(input())
Bone = B // 100
Btwo = (B % 100) // 10
Bthree = (B % 100) % 10
print(A * Bthree)
print(A * Btwo)
print(A * Bone)
print(A * B)
