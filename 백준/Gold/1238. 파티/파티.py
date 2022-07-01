from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline

student_num, way_num, village_num = map(int, input().split())
graph = defaultdict(list)

for _ in range(way_num):
    start, end, ti = map(int, input().split())
    graph[start].append((end, ti))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    times[start] = 0

    while queue:
        cur_time, cur_node = heapq.heappop(queue)

        if times[cur_node] < cur_time:
            continue

        for new_start, new_time in graph[cur_node]:
            cost = cur_time + new_time
            
            if times[new_start] > cost:
                times[new_start] = cost
                heapq.heappush(queue, (cost, new_start))
    return times

result = [[]]
for i in range(1, student_num + 1):
    # 매번 초기화해야 한 마을에 대한 최단 시간을 계산할 수 있음
    times = [int(1e9)] * (student_num + 1)
    # 한 마을에서 다른 마을까지의 최단 시간
    result.append(dijkstra(i))

time_list = []
for i in range(1, student_num+1):
    # 각자 집에서 마을까지의 최단 시간 + 마을에서 각자 집까지의 최단 시간
    time_list.append(result[i][village_num] + result[village_num][i])

print(max(time_list))
