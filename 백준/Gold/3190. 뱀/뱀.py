import sys
from collections import deque
input = sys.stdin.readline

# 보드 만들기
n = int(input())
board = [[0]*n for _ in range(n)]

# 사과 위치 정보 입력
k = int(input())
for _ in range(k):
    row, col = map(int, input().split())
    # 사과가 위치한 좌표는 1로 표시
    board[row-1][col-1] = 1

# 뱀의 방향 전환 정보 입력
rotation = []
l = int(input())
for _ in range(l):
    term, direction = input().split()
    term = int(term)
    rotation.append((term, direction))

rotation.append((10001, ''))

# 뱀 위치 이동 방향 : top, right, bottom, left
direction_change = [(-1,0), (0,1), (1,0), (0,-1)]


def turn_snake(direction):
    global turn_index

    if direction == "L":
        if turn_index != 0:
            turn_index -= 1
        else:
            turn_index = 3
    else:
        if turn_index != 3:
            turn_index += 1
        else:
            turn_index = 0
    return

# 뱀 출발 위치
snake = deque()
snake.append((0,0))

# 뱀의 출발 방향: 오른쪽
turn_index = 1

# 뱀의 머리 위치 좌표
x, y = 0, 0

# 게임 진행시간
time = 0
# 방향 바꿀 때 출발 시간
start = 1

flag = False

for i in range(len(rotation)):

    start = time + 1

    for _ in range(start, rotation[i][0] + 1):

        # 이동할 좌표
        nx = x + direction_change[turn_index][0]
        ny = y + direction_change[turn_index][1]

        # 벽 또는 자기 자신의 몸과 부딪히면 반복문 종료
        if nx < 0 or nx >= n or ny < 0 or ny >= n or (nx, ny) in snake:
            time += 1
            flag = True
            break
    
        x, y = nx, ny
        # 이동할 다음 좌표에 사과가 있는 경우
        if board[nx][ny] == 1:
            board[nx][ny] = 0
        else:
            snake.popleft()
        # 뱀의 위치 표시
        snake.append((x, y))
        # 시간 1초씩 증가
        time += 1
    if flag:
        break
    turn_snake(rotation[i][1])

print(time)