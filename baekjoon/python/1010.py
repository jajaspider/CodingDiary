import sys

T = int(sys.stdin.readline())
def fac(num):
    result = 1
    for i in range(1,num+1):
        result*=i

    return result

for _ in range(0,T):
    N,M = map(int, sys.stdin.readline().split())
    #nCm 문제
    result = fac(M)//(fac(N)*fac(M-N))
    print(result)