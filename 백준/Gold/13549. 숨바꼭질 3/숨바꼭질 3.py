import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [0] * 100001

def dijkstra(start):

    queue = []
    heapq.heappush(queue, (0, start))
    visited[start] = 1

    while queue:
        cur_time, cur_pos = heapq.heappop(queue)

        if cur_pos == k:
            print(cur_time)
            break

        for new_pos in (cur_pos*2, cur_pos+1, cur_pos-1):
            if 0 <= new_pos < 100001 and visited[new_pos] == 0:
                if new_pos == cur_pos*2:
                    visited[new_pos] = 1
                    heapq.heappush(queue, (cur_time, new_pos))
                else:
                    visited[new_pos] = 1
                    heapq.heappush(queue, (cur_time+1, new_pos))

dijkstra(n)