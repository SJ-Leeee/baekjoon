import sys
N = int(sys.stdin.readline())

def zero_one (N):
    if N < 3: 
        print(N)
        return
    dp = [0] * (N+1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, N+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
        
    print(dp[N])    
    
zero_one(N)