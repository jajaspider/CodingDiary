import itertools
import sys

while True:
    listS = list(map(int, sys.stdin.readline().split()))

    if int(listS[0]) == 0:
        break
    for result in itertools.combinations(listS[1:], 6):
        print(' '.join(map(str, result)))
    print('')
