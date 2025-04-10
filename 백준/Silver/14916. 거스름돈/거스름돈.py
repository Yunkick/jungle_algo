import sys
input = sys.stdin.readline

n = int(input())

dp = [-1] * (n+10)

dp[2]=1
dp[4]=2
dp[5]=1
dp[6]=3
dp[7]=2
dp[8]=4
dp[9]=3

for i in range(10, n+1):
    dp[i] = min(dp[i-2], dp[i-5])+1

print(dp[n])

# result = 0

# n = int(input())

# money = [5,2]

# for i in money:
#     if n == 0:
#         break
#     result += n//i
#     n %= i

# print(result)