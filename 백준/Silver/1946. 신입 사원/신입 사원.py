
import sys


N = int(sys.stdin.readline())

for _ in range(N):
    M = int(sys.stdin.readline())
    newbi = []
    for _ in range(M):
        interview, resume = map(int, sys.stdin.readline().split())
        newbi.append((interview, resume))

    newbi.sort()
    cut_line = newbi[0][1]
    cnt = 1
    for i in range(1, M):
        if newbi[i][1] < cut_line:
            cnt += 1
            cut_line = newbi[i][1]
    print(cnt)
