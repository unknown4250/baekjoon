from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())

# 상자에 저장된 토마토들의 정보
box = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

queue = deque()

# 처음에 익어있는 토마토 좌표 저장
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i, j])


def bfs():
    while queue:
        # 익은 토마토의 좌표
        x, y = queue.popleft()

        # 익은 토마토의 상하좌우 탐색
        for i in range(4):
            # 상하좌우의 좌표
            nx, ny = x + dx[i], y + dy[i]

            # 새로운 좌표가 박스 크기 넘어가면 pass
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 익지 않은 토마토를 익힘 처리
            if box[nx][ny] == 0:
                # 박스의 좌표에는 익히는 데 걸리는 시간이 저장됨
                box[nx][ny] = box[x][y] + 1
                queue.append([nx, ny])

bfs()

answer = 0
for i in range(n):
    for j in box[i]:
        # bfs 수행 후에도 익히지 못한 토마토가 있다면 -1 출력
        if j == 0:
            print(-1)
            exit(0)
    # 한 줄이 모두 다 익었다면 최댓값 선택
    answer = max(answer, max(box[i]))

print(answer - 1)
