import sys


C, K = map(int, sys.stdin.readline().split())

coins = set()
for _ in range(C):
    coin = int(sys.stdin.readline())
    coins.add(coin)

dp = [0 for _ in range(K + 1)]
dp[0] = 1
for c in coins:
    for i in range(c, K + 1):
        dp[i] = dp[i] + dp[i - c]

print(dp[-1])
