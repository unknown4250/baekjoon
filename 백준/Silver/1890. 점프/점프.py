import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 각 칸에 도착할 때마다 1씩 증가
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1


for i in range(n):
    for j in range(n):
        # 종착점에 도착하는 경우
        if i == n-1 and j == n-1:
            print(dp[i][j])
            break
        
        # 오른쪽으로 이동
        if j + graph[i][j] < n:
            dp[i][j + graph[i][j]] += dp[i][j]
        
        # 아래쪽으로 이동
        if i + graph[i][j] < n:
            dp[i + graph[i][j]][j] += dp[i][j]