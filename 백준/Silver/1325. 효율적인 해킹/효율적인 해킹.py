import collections
from operator import truediv
import sys
read = sys.stdin.readline


def bfs(x):
    queue = collections.deque()
    queue.append(x)
    visited[x] = True
    while queue:
        cur = queue.popleft()

        for node in graph[cur]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)

n, m = map(int, input().split())

graph = collections.defaultdict(list)

for _ in range(m):
    a, b = map(int, read().split())
    # 두 번째 컴퓨터를 통해 첫 번째 컴퓨터를 해킹할 수 있음(방향 그래프)
    graph[b].append(a)

cnt = []
for i in range(1, n+1):
    visited = [False] * (n+1)
    bfs(i)
    cnt.append(visited.count(True))

idx = 1
for i in cnt:
    if i == max(cnt):
        print(idx, end=' ')
    idx += 1