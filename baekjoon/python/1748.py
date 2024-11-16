N = input()
sum = 0
len_check = 1
Nlen = len(N)

while len_check < Nlen:
    sum = sum + len_check * 9 * (10 ** (len_check - 1))
    len_check += 1
tempN = int(N) - (10 ** (Nlen - 1)) + 1
sum += tempN * len(str(N))
print(sum)
