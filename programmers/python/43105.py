#https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(input):
    # array_2d = json.loads(input)
    input.reverse()
    for i in range(0,len(input)-1):
        for j in range(0,len(input[i])-1):
            input[i+1][j] = input[i+1][j] + max(input[i][j],input[i][j+1])
    return input[-1][0]
        