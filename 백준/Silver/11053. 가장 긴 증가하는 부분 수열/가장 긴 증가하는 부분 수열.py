import bisect

n = int(input())
arr = list(map(int, input().split()))

# LIS를 저장할 리스트
dp = []

for num in arr:
    # 현재 수가 들어갈 위치를 이분 탐색
    idx = bisect.bisect_left(dp, num)
    
    # 해당 위치가 dp의 끝보다 작으면 덮어 씌운다
    if idx == len(dp):
        dp.append(num)
    else:
        dp[idx] = num

# LIS의 길이 출력
print(len(dp))
