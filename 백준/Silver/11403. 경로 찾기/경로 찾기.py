import collections
import sys
input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

queue = collections.deque()

# bfs 방식
for i in range(n):
    queue.append(i)

    while queue:
        cur = queue.popleft()

        # 현재 정점의 인접 정점 확인
        for j in range(len(graph[cur])):
            # 연결된 정점 중 방문하지 않은 정점에 대해 bfs 수행
            if graph[cur][j] == 1 and not visited[i][j]:
                # 방문 여부 표시
                visited[i][j] = True
                # 다음으로 탐색할 정점
                queue.append(j)

for i in range(n):
    for j in range(n):
        if visited[i][j]:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()

