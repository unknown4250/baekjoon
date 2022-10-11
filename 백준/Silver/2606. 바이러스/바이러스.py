import sys
read = sys.stdin.readline

n = int(read())
e = int(read())

graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(e):
    src, dst = map(int, read().split())
    graph[src][dst] = graph[dst][src] = 1

visited = []
def dfs(start):
    visited.append(start)
    for w in range(len(graph[start])):
        if (w not in visited) and graph[start][w] == 1:
            dfs(w)

dfs(1)
print(len(visited) - 1)