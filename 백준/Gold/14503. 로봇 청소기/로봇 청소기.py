import sys
input = sys.stdin.readline

# 세로 크기, 가로 크기
n, m = map(int, input().split())

# 북, 동, 남, 서(시계 방향)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 청소 표시
visited = [[0] * m for _ in range(n)]

# 로봇청소기 위치, 바라보는 방향
x, y, d = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(n)]

# 로봇 청소기 현재 위치로 이동 표시
visited[x][y] = 1 

# 초기 위치 청소
cnt = 1

while True:
    flag = False # 청소 여부 확인 플래그
    
    # 4방향 회전
    for _ in range(4):
        # 왼쪽 방향으로 회전
        d = (d + 3) % 4

        # 로봇 청소기가 이동하려는 좌표
        nx = x + dx[d]
        ny = y + dy[d]

        # 새로운 좌표가 범위 내에 있고, 벽이 아닌 경우(=빈칸인 경우)
        if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 0:

            # 이동하려는 좌표가 청소 안 됐으면
            if visited[nx][ny] == 0:
                # 해당 위치 청소
                visited[nx][ny] = 1
                # 청소 칸 추가
                cnt += 1
                # 로봇청소기 위치 이동
                x, y = nx, ny
                # 청소 여부 표시
                flag = True
                break
    
    # 네 방향 모두 청소할 구역이 없는 경우
    if not flag:
        # 현재 위치에서 향하고 있는 방향을 빼면 후진한 x, y 좌표
        nx = x - dx[d]
        ny = y - dy[d]

        # 후진했을 때 빈칸이면 이동 가능
        if maps[nx][ny] == 0:
            x, y = nx, ny
        # 후진했을 때 벽이면 이동 불가능, 종료
        else:
            print(cnt)
            break
