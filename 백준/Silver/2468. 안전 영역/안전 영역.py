import collections
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
max_depth = -1

space = []
for i in range(n):
    # 지역의 높이 정보 입력
    space.append(list(map(int, input().split())))
    # 최대 높이
    max_depth = max(max_depth, max(space[i]))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, depth, visited):
    queue = collections.deque()
    queue.append((x, y))    # 큐에 시작점 추가
    visited[x][y] = True    # 시작점의 방문 표시

    while queue:
        cur_x, cur_y = queue.popleft()

        # 인접한 영역은 하나의 영역으로 간주    
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            # 범위를 벗어나지 않으면서 방문하지 않은 위치라면
            if 0 <= nx < n and 0 <= ny < n and (not visited[nx][ny]):
                # 기준보다 높은 영역인지 확인
                if space[nx][ny] > depth:
                    visited[nx][ny] = True  # 방문 표시
                    queue.append((nx, ny))  # 인접한 영역 살펴보기 위해 탐색할 위치로 추가

answer = 0

# 아무 곳도 물에 안 잠길 수 있으므로 0 ~ max_depth-1 범위를 탐색
for i in range(max_depth):
    visited = [[False] * n for i in range(n)]
    cnt = 0

    for j in range(n):
        for k in range(n):
            # 방문하지 않았으면서 기준 높이보다 높은 경우
            if (not visited[j][k]) and space[j][k] > i:
                bfs(j, k, i, visited)
                # 안전한 영역 추가
                cnt += 1
    # 최대 개수
    if answer < cnt:
        answer = cnt

print(answer)