N = int(input())

count = 0
num = 0
while True:
    if count == N:
        print(num)
        break
    num += 1
    if "666" in str(num):
        count += 1
