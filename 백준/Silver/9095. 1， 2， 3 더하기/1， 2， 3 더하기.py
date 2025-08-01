import sys


def sum_only_123(n):
    if n <= 2:
        return n
    elif n == 3:
        return 4
    dp = [-1] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]


N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    print(sum_only_123(num))
