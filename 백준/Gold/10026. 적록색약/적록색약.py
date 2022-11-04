import collections
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

visited = [[False] * n for _ in range(n)]
board = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, color):
    queue = collections.deque()
    queue.append((x,y))

    while queue:
        cur_x, cur_y = queue.popleft()

        # 방문한 위치라면 pass
        if visited[cur_x][cur_y]:
            continue

        # 방문 표시
        visited[cur_x][cur_y] = True

        # 인접한 위치 탐색
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            # 그리드를 벗어나지 않으면서 같은 색상이라면 다음 탐색 위치
            if nx >= 0 and nx < n and ny >= 0 and ny < n and board[nx][ny] == color:
                queue.append((nx, ny))


# 적록색약이 아닌 사람(빨강, 초록, 파랑 -> 3가지 색 구분)
normal = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, board[i][j])
            normal += 1

# 적록색약은 빨강과 초록을 같은 색으로 인식
for i in range(n):
    for j in range(n):
        # 초록색이라면 해당 위치를 빨강색으로 변경
        if board[i][j] == 'G':
            board[i][j] = 'R'

# 방문 표시 초기화
visited = [[False] * n for _ in range(n)]

# 적록색약인 사람(빨강/초록, 파랑 -> 2가지 색 구분)
stranger = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, board[i][j])
            stranger += 1

print(normal, stranger)