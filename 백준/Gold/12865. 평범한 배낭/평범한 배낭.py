
import sys


I, K = map(int, sys.stdin.readline().split())
items = []
for _ in range(I):
    kg, val = map(int, sys.stdin.readline().split())
    items.append((kg, val))

dp = [[0 for _ in range(K + 1)] for _ in range(len(items) + 1)]


for i in range(1, len(items) + 1):
    kg, val = items[i - 1]
    for k in range(K + 1):
        if kg > k:
            dp[i][k] = dp[i - 1][k]
        else:
            dp[i][k] = max(dp[i - 1][k - kg] + val, dp[i - 1][k])

print(dp[-1][-1])
