
import sys

# {10, 20, 30, 15, 20, 30, 50, 40, 45 ,60}

lis = []

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

lis.append(arr[0])

for i in range(1, len(arr)):
    if lis[-1] < arr[i]:
        lis.append(arr[i])
    else:
        right = len(lis)
        left = 0

        while left < right:
            mid = (right + left) // 2

            if lis[mid] < arr[i]:  # arr[i] 15가 크다면
                left = mid + 1
            else:
                right = mid
        lis[left] = arr[i]

print(len(lis))

