import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

dp = [0] * n

if n == 1:
    print(nums[0])
elif n == 2:
    print(nums[0] + nums[1])
else:
    dp[0] = nums[0]
    dp[1] = nums[0] + nums[1]
    dp[2] = max(nums[0]+nums[2], nums[1]+nums[2], dp[1])

    for i in range(3, n):
        # 포도주를 마시는 경우는 아래 3가지
        # 현재 포도주 + 전전 포도주까지 마신 양
        # 현재 포도주 + 전 포도주 + 3번째 전 포도주까지 마신 양
        # 전 포도주까지 마신 양 (*** 중요, 현재 포도주를 포함하지 않는 경우)
        dp[i] = max(nums[i]+dp[i-2], nums[i-1]+nums[i]+dp[i-3], dp[i-1])

    print(max(dp))