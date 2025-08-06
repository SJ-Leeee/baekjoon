import sys


S = int(sys.stdin.readline())

for _ in range(S):
    C = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    num = int(sys.stdin.readline())

    dp = [0] * (num + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(num + 1):
            if i >= coin:
                dp[i] += dp[i - coin]

    print(dp[-1])

