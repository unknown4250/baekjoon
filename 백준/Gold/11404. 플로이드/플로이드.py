import sys
input = sys.stdin.readline

n, m = int(input()), int(input())

# 모든 비용은 무한대로 초기화
maps = [[int(1e9)] * (n+1) for _ in range(n+1)]

# 시작점과 도착점이 같은 경우는 0
for i in range(1, n + 1):
    maps[i][i] = 0

# 같은 노선이지만 비용이 다른 경우 있으므로 가장 적은 비용 저장
for _ in range(m):
    a, b, c = map(int, input().split())
    if maps[a][b] > c:
        maps[a][b] = c

# i~j 경로와 i~k~j 경로의 비용 비교
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            maps[i][j] = min(maps[i][j], maps[i][k] + maps[k][j])

# 모든 도시의 최소 비용 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if maps[i][j] == int(1e9):
            print(0, end=" ")
        else:
            print(maps[i][j], end=" ")
    print()