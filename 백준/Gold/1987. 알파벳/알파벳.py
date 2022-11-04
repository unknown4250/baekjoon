import sys
input = sys.stdin.readline

r, c = map(int, input().split())

# 보드 정보 입력
board = [list(input().strip()) for _ in range(r)]

visited = [0] * 26 # 방문했던 알파벳(시간 효율성을 위해 배열 사용)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 1

def bfs(x, y):
    global answer

    queue = set([(x, y, board[x][y])])

    while queue:
        # 현재 위치 좌표, 이동 경로
        cur_x, cur_y, result = queue.pop()

        # 상하좌우 탐색
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            # 보드 범위 벗어나면 pass
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue

            # 현재 위치의 알파벳이 지나온 알파벳에 없다면
            if board[nx][ny] not in result:
            
                # 현재 위치와 이동 경로 추가
                queue.add((nx, ny, result + board[nx][ny]))

                # 이동 거리가 최대 값인지 확인
                answer = max(answer, len(result)+1)


# dfs 수행
bfs(0, 0)

# 결과 출력
print(answer)