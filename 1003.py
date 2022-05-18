import sys
input = sys.stdin.readline
zero = [1, 0, 1]
one = [0, 1, 1]

def fibo(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print('{} {}'.format(zero[num], one[num]))

T = int(input())

for _ in range(0,T):
    fibo(int(input()))