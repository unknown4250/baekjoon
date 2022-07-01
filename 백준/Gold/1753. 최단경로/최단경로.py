from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

# 정점 개수, 간선 개수
vertex_num, edge_num = map(int, input().split())

# 시작 정점
start_vertex = int(input())

# 경로 그래프
graph = defaultdict(list)

# 최대값으로 가중치 초기화
weights = [int(1e9)] * (vertex_num + 1)

# 경로 그래프 구축
for _ in range(edge_num):
    # 출발 정점, 도착 정점, 가중치
    start, end, weight = map(int, input().split())
    
    # 출발 정점을 기준으로 그래프에 값 저장
    graph[start].append((end, weight))


def dijkstra(start):
    queue = []

    # 시작점을 큐에 넣기
    heapq.heappush(queue, (0, start))

    # 시작점의 가중치를 0으로 초기화
    weights[start] = 0

    # 연결 정보가 없을 때까지 반복
    while queue:

        # 현재 정점과 가중치
        cur_weight, cur_node  = heapq.heappop(queue)

        # 현재 가중치가 연결된 정점에 의한 가중치 합보다 크면 저장할 필요 없음
        if weights[cur_node] < cur_weight:
            continue

        # 현재 정점의 인접 정점 탐색
        for new_start, new_weight in graph[cur_node]:

            # 현재 정점과 인접 정점의 가중치 합 
            cost = cur_weight + new_weight
            
            # 인접 정점의 가중치보다 현재 정점 가중치 + 인접 정점 가중치가 더 작으면 업데이트
            if cost < weights[new_start]:
                weights[new_start] = cost

                # 인접 정점을 다음에 탐색하기 위해 큐에 저장
                heapq.heappush(queue, (cost, new_start))


dijkstra(start_vertex)

for i in range(1, vertex_num + 1):
    # 초기값이 갱신되지 않았다면 경로가 없는 경우
    if weights[i] == int(1e9):
        print("INF")
    # 시작점으로부터 i번 정점으로의 최단 경로 가중치
    else:
        print(weights[i])