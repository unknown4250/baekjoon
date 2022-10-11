import collections
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x):
    if visited[x]:
        return

    visited[x] = True

    for y in range(1, len(graph[x])):
        if graph[x][y] == 1:
            dfs(y)


n, m = map(int, read().split())

graph = [[0]*(n+1) for _ in range(n+1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, read().split())
    graph[u][v] = graph[v][u] = 1

cnt = 0

for i in range(1, n + 1):
    if not visited[i]:
        cnt += 1
        dfs(i)

print(cnt)