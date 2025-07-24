import sys


N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
sangeun_data = list(map(int, sys.stdin.readline().split()))

data.sort()
result = []
for i in range(M):
    start = 0
    end = len(data)

    while start < end:
        mid = (start + end) // 2

        if sangeun_data[i] > data[mid]:
            start = mid + 1
        else:
            end = mid

    if start < N and sangeun_data[i] == data[start]:
        result.append(1)
    else:
        result.append(0)

print(*result)
