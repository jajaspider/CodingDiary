import sys

N, L = map(int, sys.stdin.readline().split())

def solve():
    for i in range(L,101):
        x = N/i-(i+1)/2
        if float(x)%1==0:
            if x>=-1:
                return int(x+1),i
  
try:
    count, start = solve()
    print(" ".join(map(str, list(range(count,count+start)))))
except Exception as e:
    print(-1)