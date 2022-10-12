import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n = map(int, read().split())

# dfs + dp
graph = [list(map(int, read().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    # 제일 오른쪽 아래 칸에 도착한 경우
    if x == m - 1 and y == n - 1:
        return 1
    
    # 방문한 경우
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < m and 0 <= ny < n:
            # 현재 위치보다 이동할 위치의 값이 작아야 이동 가능
            if graph[x][y] > graph[nx][ny]:
                dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]

print(dfs(0, 0))