def solution():
    '''
    N = int(input())
    Nnumbers = list(map(int, input().split()))
    M = int(input())
    Mnumbers = list(map(int, input().split()))
    Nnumbers.sort()

    for i in range(0, M):
        first = 0
        last = N
        while first < last:

            mid = (first + last) // 2

            if Nnumbers[mid] == Mnumbers[i]:
                print("1")
                break

            elif Nnumbers[mid] < Mnumbers[i]:
                first = mid + 1
            elif Nnumbers[mid] > Mnumbers[i]:
                last = mid - 1
            if last < N and 0 <= first:
                if Nnumbers[first] == Mnumbers[i] or Nnumbers[last] == Mnumbers[i]:
                    print("1")
                    break
        if first >= last:
            print("0")
            '''
    N = int(input())
    A = {i: 1 for i in map(int, input().split())}
    M = input()
    for i in map(int, input().split()):
        print(A.get(i, 0))


solution()
