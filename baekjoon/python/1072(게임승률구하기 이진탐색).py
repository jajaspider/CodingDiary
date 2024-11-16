import math

# x는 게임횟수
# x = 53
# y는 이긴게임
# y = 47
x, y = map(int, input().split())
rate = int(y * 100 / x)
temp = rate

if rate >= 99:
    print("-1")
    exit()

first = 0
last = 1000000000
result = 0
while first <= last:
    mid = int((first + last) / 2)

    temp = int((y + mid) * 100 / (x + mid))
    if temp > rate:
        last = mid - 1
    else:
        first = mid + 1
        result = mid + 1

print(result)
