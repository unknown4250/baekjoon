import sys
input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n+1)]

arr = [list(map(int, input().split())) for _ in range(n)]

# 마지막 날부터 비교
for i in range(n-1, -1, -1):
    # 상담이 끝나는 날이 n을 넘어갈 수 없음
    if i + arr[i][0] > n:
        # 퇴사 이후라면 현재 상담 비용이 이후의 비용
        dp[i] = dp[i+1]
    # i일 건너뛰고 i+1일에 받는 비용, i일에 받는 비용 + i일에 걸리는 시간 이후 날짜의 이익
    else:
        dp[i] = max(dp[i+1], arr[i][1]+dp[i+arr[i][0]])

print(dp[0])