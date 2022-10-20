import collections
from hashlib import new
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

size = 2 # 상어 초기 크기
shark_x, shark_y = 0, 0

# 상어 위치 찾기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark_x = i
            shark_y = j

def bfs(x, y, shark_size):    
    # 거리 : 아기 상어 위치에서 물고기 위치로 이동할 때 지나가야 하는 최단 경로의 칸 개수
    dist = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    queue = collections.deque()
    queue.append((x, y))
    visited[x][y] = True     # 현재 위치 방문 표시

    tmp = []

    while queue:
        cur_x, cur_y = queue.popleft()

        # 상하좌우로 이동
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            # 공간의 범위를 벗어나지 않으면서 방문하지 않은 위치의 경우
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 아기 상어 크기가 물고기 크기보다 크거나 작으면 해당 칸으로 이동 가능
                if graph[nx][ny] <= shark_size:
                    queue.append((nx, ny))
                    visited[nx][ny] = True # 방문 표시
                    dist[nx][ny] = dist[cur_x][cur_y] + 1 # 이동 거리 증가

                    # 빈칸이 아니면서 물고기 크기가 아기 상어보다 작은 경우,
                    # 다음으로 이동할 칸 후보가 됨
                    if graph[nx][ny] < shark_size and graph[nx][ny] != 0:
                        tmp.append((nx, ny, dist[nx][ny]))

    # 1)거리가 가장 가까운 물고기, 2)가장 위에 있는 물고기, 3)가장 왼쪽에 있는 물고기 순으로 선택하도록 정렬
    return sorted(tmp, key=lambda x: (-x[2], -x[0], -x[1]))

cnt = 0
time = 0

while True:
    # 현재 위치에서 먹을 수 있는 물고기 탐색
    shark = bfs(shark_x, shark_y, size)

    # 더 이상 먹을 수 있는 물고기가 없으면 엄마 상어에게 도움을 요청
    if len(shark) == 0:
        break

    new_x, new_y, distance = shark.pop()

    # 움직인 칸 수 = 시간
    time += distance
    graph[shark_x][shark_y], graph[new_x][new_y] = 0, 0

    # 상어 좌표를 먹은 물고기의 좌표로 변경
    shark_x, shark_y = new_x, new_y

    # 물고기 먹은 횟수 증가
    cnt += 1

    # 자신의 크기와 같은 수의 물고기를 먹으면 크기 1 증가
    if cnt == size:
        size += 1
        cnt = 0

print(time)
