import sys


N = int(sys.stdin.readline())

coins = [2, 5]

coin_dp = [float("inf")] * (N + 1)

coin_dp[0] = 0


for i in range(2, N + 1):
    if i < 5:
        coin_dp[i] = coin_dp[i - 2] + 1
    else:
        coin_dp[i] = min(coin_dp[i - 2] + 1, coin_dp[i - 5] + 1)

result = coin_dp[-1] if coin_dp[-1] != float("inf") else -1
print(result)
