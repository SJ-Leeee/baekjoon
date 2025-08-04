import sys

N = int(sys.stdin.readline())

data = []
for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    data.append((start, end))

data.sort(key=lambda x: (x[1], x[0]))  # 끝나는시간 먼저, 같으면 시작시간이 먼저
end_point = -1
result = 0
for start, end in data:
    if start >= end_point:
        result += 1
        end_point = end

print(result)
