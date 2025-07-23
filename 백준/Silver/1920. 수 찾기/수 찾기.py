import sys

N = int(sys.stdin.readline())
standard_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

standard_list.sort()
arr = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    right = len(standard_list)
    left = 0

    while left < right:
        mid = (right + left) // 2

        if standard_list[mid] < arr[i]:
            left = mid + 1
        else:
            right = mid

    if left < N and standard_list[left] == arr[i]:
        print(1)
    else:
        print(0)