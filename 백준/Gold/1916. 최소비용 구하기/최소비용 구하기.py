from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    queue = []

    # 시작 비용을 0으로 설정
    heapq.heappush(queue, (0, start))

    while queue:
    
        # 탐색할 노드와 버스 비용
        cur_cost, cur_node = heapq.heappop(queue)

        # 기존 비용보다 많으면 체크할 필요 없음
        if costs[cur_node] < cur_cost:
            continue
        
        # 현재 노드와 인접한 노드 방문
        for new_start, new_cost in graph[cur_node]:
            
            # 해당 노드를 지나갈 때의 비용
            cost = cur_cost + new_cost

            # 현재 알고있는 비용보다 적으면 해당 값으로 업데이트
            if costs[new_start] > cost:
                costs[new_start] = cost

                # 다음 인접 노드의 비용 계산을 위해 큐에 삽입
                heapq.heappush(queue, (cost, new_start))


city_num = int(input()) # 도시 개수
bus_num = int(input())  # 버스 개수

graph = defaultdict(list)

# 버스 비용 정보
costs = [int(1e9)] * (city_num + 1)

# 출발지, 도착지, 버스비용 저장
for _ in range(bus_num):
    departure, destination, fee = map(int, input().split())
    graph[departure].append((destination, fee))

departure_city, destination_city = map(int, input().split())   # 출발점의 도시 번호, 도착점의 도시 번호

dijkstra(departure_city) # 출발점으로부터 모든 도시까지의 최소 비용 그래프 구축
print(costs[destination_city])