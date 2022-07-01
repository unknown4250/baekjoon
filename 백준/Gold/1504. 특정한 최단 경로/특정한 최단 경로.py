from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline

v, e = map(int, input().split())
graph = defaultdict(list)

for _ in range(e):
    start, end, dist = map(int, input().split())
    graph[start].append((end, dist))
    graph[end].append((start, dist))


def dijkstra(start):
    distances = [int(1e9)] * (v + 1)

    queue = []
    heapq.heappush(queue, (0, start))
    distances[start] = 0

    while queue:
        cur_dist, cur_node = heapq.heappop(queue)

        if distances[cur_node] < cur_dist:
            continue

        for new_node, new_dist in graph[cur_node]:
            temp_dist = cur_dist + new_dist
            
            if distances[new_node] > temp_dist:
                distances[new_node] = temp_dist
                heapq.heappush(queue, (temp_dist, new_node))

    return distances

# 반드시 거쳐야 하는 두 개의 정점
v1, v2 = map(int, input().split())

one_node_distance = dijkstra(1) # 1번 정점에서 모든 정점까지의 최단 경로
v1_distance = dijkstra(v1)      # v1에서 모든 정점까지의 최단 경로
v2_distance = dijkstra(v2)      # v2에서 모든 정저맊지의 최단 경로

# 경로 : 1 → v1 → v2 → N or 1 → v2 → v1 → N
# 1번 정점에서의 v1까지의 최단 경로 + v1에서 v2까지의 최단 경로 + v2에서 N 까지의 경로
# 1번 정점에서의 v2까지의 최단 경로 + v2에서 v1까지의 최단 경로 + v1에서 N 까지의 경로
v1_path = one_node_distance[v1] + v1_distance[v2] + v2_distance[v]
v2_path = one_node_distance[v2] + v2_distance[v1] + v1_distance[v]

# 두 경로 중 최소값 선택
result = min(v1_path, v2_path)

print(result if result < int(1e9) else -1)
