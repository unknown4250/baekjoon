import collections
import heapq
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

# 그래프 구축
graph = collections.defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    # 단방향 그래프
    graph[a].append(b)

queue = []
nodes = [] # 최단 거리가 k인 도시 저장
visited = [False] * (n + 1) # 방문 확인 배열

# 시작점 큐에 넣기
heapq.heappush(queue, (0, x))

while queue:
    cur_dist, cur_node = heapq.heappop(queue)
    
    # 방문했던 도시라면 재방문 X
    if visited[cur_node]:
        continue

    # 방문 표시
    visited[cur_node] = True

    # x부터의 이동 거리가 k라면 결과 배열에 추가
    if cur_dist == k:
        nodes.append(cur_node)
        continue

    # 인접한 도시 탐색
    for next_node in graph[cur_node]:
        # 다른 도시로 이동할 때마다 거리 1씩 증가
        heapq.heappush(queue, (cur_dist + 1, next_node))

nodes.sort()
# 이동 거리 k인 도시 있다면 도시 번호 출력
if len(nodes) > 0:
    for node in nodes:
        print(node)
# 없다면 -1 출력
else:
    print(-1)