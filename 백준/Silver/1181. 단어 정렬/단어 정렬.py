import sys

N = int(input())
duplicate_data = [sys.stdin.readline().strip()for i in range(N)]
data=list(set(duplicate_data))
data.sort(key=lambda x:(len(x), x))

for i in data:
    print(i)
