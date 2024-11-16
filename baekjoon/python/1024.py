import sys

N, M = map(int, sys.stdin.readline().split())
target =list(map(int, sys.stdin.readline().split())) 

print(N,M)
print(target)

queue = [ i for i in range(1,N+1)]
print(queue)
