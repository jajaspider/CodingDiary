from collections import Counter
import sys


def merget_Sort(x):
    if len(x) <= 1:
        return x
    left = merget_Sort(x[:len(x) // 2])
    right = merget_Sort(x[len(x) // 2:])

    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            x[k] = left[i]
            i += 1
        else:
            x[k] = right[j]
            j += 1
        k += 1
    if i == len(left):
        while j < len(right):
            x[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            x[k] = left[i]
            i += 1
            k += 1
    return x


def average(sort_list):
    return round(sum(sort_list) / len(sort_list))


def mean(sort_list):
    return sort_list[int((len(sort_list) - 1) / 2)]


def mode(sort_list):
    if N ==1:
        return sort_list[0]
    c_list = Counter(sort_list).most_common(2)
    if c_list[0][1] == c_list[1][1]:
        return c_list[1][0]
    else:
        return c_list[0][0]


def ran(sort_list):
    if len(sort_list) == 1:
        return 0
    if sort_list[0] < 0 and sort_list[-1] < 0:
        return abs(sort_list[0] + abs(sort_list[-1]))
    else:
        return abs(sort_list[0]) + abs(sort_list[-1])


numberlist = []
N = int(sys.stdin.readline())
for i in range(0, N):
    numberlist.append(int(sys.stdin.readline()))
numberlist_sort = sorted(numberlist)
# numberlist_sort = merget_Sort(numberlist)
print(average(numberlist_sort))
print(mean(numberlist_sort))
print(mode(numberlist_sort))
print(ran(numberlist_sort))
