N = int(input())
weight = []

for i in range(0, N):
    weight.append(input().split())

rank = []
for i in range(0, N):
    count = 1
    for j in range(0, N):
        if weight[i][0] < weight[j][0] and weight[i][1] < weight[j][1]:
            count += 1
    rank.append(count)

for i in rank:
    print(i, end=" ")
