import sys

NAMES = sys.stdin.readline().replace("\n", "")
noun = []
nouncount = []
for i in range(0, len(NAMES)):
    if NAMES[i] in noun:
        nouncount[noun.index(NAMES[i])] = int(nouncount[noun.index(NAMES[i])]) + int(1)
    else:
        noun.append(NAMES[i])
        nouncount.append(1)

oddcount = 0
for i in range(0, len(nouncount)):
    if nouncount[i] % 2 == 1:
        oddcount += 1
if oddcount >= 2:
    print("I'm Sorry Hansoo")
    exit()

noun_list = {}
for i in noun:
    noun_list.setdefault(i, nouncount[noun.index(i)])
noun_list_sort = sorted(noun_list.items())

for i in noun_list_sort:
    if i[1] % 2 == 1:
        oddalpha = i[0]
        oddalphacount = i[1]

left = []
center = []
for i in noun_list_sort:
    for j in range(0, int(i[1])//2):
        left.append(i[0])
    if i[1] % 2 == 1:
        center.append(i[0])
right = list(reversed(left))
for i in left + center + right:
    print(i, end="")
