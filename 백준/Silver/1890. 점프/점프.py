import sys


N = int(sys.stdin.readline())

s_map = []
s_dp = [[0 for _ in range(N)] for _ in range(N)]

s_dp[0][0] = 1
for _ in range(N):
    item = list(map(int, sys.stdin.readline().split()))
    s_map.append(item)

for row in range(N):
    for col in range(N):
        if s_map[row][col] == 0:
            continue
        if row == N - 1 and col == N - 1:
            break

        jump = s_map[row][col]  # 점프할 개수
        down = row + jump  # 아래로 점프
        right = col + jump

        if right < N:
            s_dp[row][right] += s_dp[row][col]
        if down < N:
            s_dp[down][col] += s_dp[row][col]

print(s_dp[N - 1][N - 1])