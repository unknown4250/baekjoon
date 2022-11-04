import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

t = int(input())


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):

    # 배추가 없으면 탐색 X
    if graph[x][y] == 0:
        return

    # 중복 탐색하지 않기 위해 0으로 표시
    graph[x][y] = 0

    # 인접한 위치에 배추가 있는지 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 배추밭 범위 벗어나면 pass
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        
        # 인접한 위치에도 배추 있으면
        if graph[nx][ny] == 1:
            # 해당 위치를 기준으로 dfs 수행
            dfs(nx, ny)


for _ in range(t):
    # 가로 길이, 세로 길이, 배추 개수
    m, n, k = map(int, input().split())

    # 배추밭 (N x M)
    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        # 배추가 심어진 위치
        y, x = map(int, input().split())
        graph[x][y] = 1 # 1로 표시

    count = 0
    
    for i in range(n):
        for j in range(m):
            # 배추가 심어진 위치 
            if graph[i][j] == 1:
                dfs(i, j)
                # dfs가 끝나면 인접한 배추 모두 센 것 => 지렁이 1개 필요
                count += 1

    print(count)
    

