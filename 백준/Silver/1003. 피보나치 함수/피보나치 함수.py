import sys
T = int(sys.stdin.readline())
dp = [0] * 50
dp[1] = 1
dp[2] = 1

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    if dp[n] != 0:
        return dp[n]

    dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]

    
for _ in range(T):
    N = int(sys.stdin.readline())
    if N == 0:
        print(1 ,0)

    elif N == 1:
        print(0,1)
    


    else:
        fibo(N)
        print(dp[N-1],dp[N])