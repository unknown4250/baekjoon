import collections
import heapq
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

# 1번 노드에서 i번 노드까지 k개의 최단 경로만 저장
distances = [[int(1e9)] * k for _ in range(n + 1)]

# 연결 정보 그래프
graph = collections.defaultdict(list)

# 연결 정보 그래프 구축
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    # 출발점의 첫 번째 경로
    distances[start][0] = 0

    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        # 현재 노드까지의 시간, 현재 노드 번호
        cur_dist, cur_node = heapq.heappop(queue)

        # 인접 노드 탐색
        for new_node, new_dist in graph[cur_node]:
            # 인접 노드의 경로 = 현재 노드까지의 시간 + 현재 노드 ~ 인접 노드 시간
            dist = cur_dist + new_dist
            # k번째 최단 경로보다 현재까지의 경로가 더 짧다면 변경
            if distances[new_node][k-1] > dist:
                distances[new_node][k-1] = dist
                # 매번 정렬해야 k-1 인덱스로 최단 경로 접근 가능
                distances[new_node].sort()
                # 큐에 탐색할 노드 추가
                heapq.heappush(queue, (dist, new_node))

# 1번 도시에서 모든 도시로 가는 최단 경로 맵 만들기
dijkstra(1)

# 1번 도시에서 i번 도시로 가는 k번째 최단 경로의 소요시간
for i in range(1, n+1):
    if distances[i][k-1] == int(1e9):
        print(-1)
    else:
        print(distances[i][k-1])