import heapq

def dijkstra(start):
    queue = []

    # 시작점의 시간을 0으로 초기화
    heapq.heappush(queue, (0, start))
    times[start] = 0

    while queue:
        cur_time, cur_node = heapq.heappop(queue)
        
        # 현재 위치가 목적지이면 걸린 시간 출력하고 탐색 종료
        if cur_node == k:
            print(cur_time)
            break
    
        # 현재 위치까지 걸린 시간이 기존 계산 시간보다 많으면 탐색할 필요 없음
        if times[cur_node] < cur_time:
            continue
        
        # 다음 위치 찾기
        # 다음 위치의 경우의 수는 (현재 위치-1, 현재위치+1, 현재위치*2)
        for new_node in (cur_node - 1, cur_node + 1, cur_node * 2):

            # 현재 위치까지 걸린 시간이 새로운 위치까지 걸린 시간보다 적으면 업데이트 
            if 0 <= new_node <= 100000 and cur_time < times[new_node]:
                # 순간이동 하는 경우
                if new_node == cur_node * 2:
                    # 걸린 시간 0초
                    times[new_node] = cur_time
                    heapq.heappush(queue, (cur_time, new_node))

                # 걸어서 이동하는 경우
                else:
                    # 걸린 시간 1초
                    times[new_node] = cur_time + 1
                    heapq.heappush(queue, (cur_time + 1, new_node))

n, k = map(int, input().split())

times = [int(1e9)] * 100001

dijkstra(n)