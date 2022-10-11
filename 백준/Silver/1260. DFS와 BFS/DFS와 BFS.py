from collections import deque
import sys
read = sys.stdin.readline

n, m, v = map(int, read().split())
graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    src, dst = map(int, read().split())
    graph[src][dst] = graph[dst][src] = 1

visited = [False] * (n+1)

def dfs(start):
    visited[start] = True
    print(start, end=' ')

    for w in range(1, n+1):
        if (not visited[w]) and graph[start][w] == 1:
            dfs(w)


def bfs(start):
    visited[start] = True

    queue = deque()
    queue.append(start)

    while queue:
        cur_vertex = queue.popleft()
        print(cur_vertex, end=' ')

        for w in range(1, n+1):
            if (not visited[w]) and graph[cur_vertex][w] == 1:
                queue.append(w)
                visited[w] = True
            

dfs(v)
print()
visited = [False] * (n+1)

bfs(v)