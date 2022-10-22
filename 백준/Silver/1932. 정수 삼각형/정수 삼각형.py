import sys
input = sys.stdin.readline

n = int(input())
dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i] = list(map(int, input().split()))

# 아래층으로 가면서 누적합 구하기
for i in range(1, n):
    for j in range(i+1):
        # 각 층의 첫 번째 값은 바로 위 값만 누적 가능
        if j == 0:
            dp[i][j] += dp[i-1][j]
        # 각 층의 마지막 값은 왼쪽 상단 값만 누적 가능    
        elif j == i:
            dp[i][j] += dp[i-1][j-1]
        # 왼쪽 상단 값과 바로 위 값 중 큰 값을 선택
        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

# 각 경로에 의해 구해질 수 있는 누적 합 중 가장 큰 값 출력
print(max(dp[n-1]))