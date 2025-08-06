
import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

lis = [data[0]]
for i in range(1, len(data)):
    if data[i] > lis[-1]:
        lis.append(data[i])
    else:
        left = 0
        right = len(lis)

        while left < right:
            mid = (left + right) // 2

            if data[i] > lis[mid]:
                left = mid + 1
            else:
                right = mid

        lis[left] = data[i]


print(len(lis))
