N = int(input())
team1_score = 0
team2_score = 0
team1_time = 0
team2_time = 0
now_time = 0
flag = 0
for i in range(0, N):
    n1, n2 = map(str, input().split(" "))
    # if now_time == 0:
    #     now_time = int(n2.split(":")[0]) * 60 + int(n2.split(":")[1])

    if int(n1) == 1:
        team1_score += 1
    if int(n1) == 2:
        team2_score += 1

    if flag == 1:
        if team1_score >= team2_score:
            team1_time += (int(n2.split(":")[0]) * 60 + int(n2.split(":")[1]) - now_time)

    if flag == 2:
        if team1_score <= team2_score:
            team2_time += (int(n2.split(":")[0]) * 60 + int(n2.split(":")[1]) - now_time)

    now_time = int(n2.split(":")[0]) * 60 + int(n2.split(":")[1])

    if team1_score > team2_score:
        flag = 1
    elif team1_score < team2_score:
        flag = 2
    else:
        flag = 0

if flag == 1:
    team1_time += (48 * 60 - now_time)
elif flag == 2:
    team2_time += (48 * 60 - now_time)
print("%02d:%02d" % (int(team1_time / 60), team1_time % 60))
print("%02d:%02d" % (int(team2_time / 60), team2_time % 60))
