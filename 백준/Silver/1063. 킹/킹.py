from sys import stdin
input = stdin.readline

king, stone, n = map(str, input().split())

# 알파벳을 숫자 좌표로 변경(A→0, B→1, ...)
king_x, king_y = int(ord(king[0]) - 64), int(king[1])
stone_x, stone_y = int(ord(stone[0]) - 64), int(stone[1])

# 움직이는 횟수
n = int(n)

# 이동 방법에 따라 변경되는 좌표 이동 값 (x좌표, y좌표)
move = {
        "R":(1, 0), "L": (-1, 0), "B": (0, -1),
        "T":(0, 1), "RT": (1, 1), "LT": (-1, 1),
        "RB": (1, -1), "LB": (-1, -1)
       }

for _ in range(n):
    # 이동 방법
    cmd = input().strip()

    # 이동 변위
    dx, dy = move[cmd][0], move[cmd][1]

    # 킹이 이동할 위치
    nx, ny = dx + king_x, dy + king_y

    # 킹의 새로운 위치가 체스판 벗어날 경우
    if nx > 8  or ny > 8 or nx < 1 or ny < 1:
        continue

    # 이동할 위치에 돌이 있는 경우
    if nx == stone_x and ny == stone_y:
        # 킹이나 돌이 체스판 벗어날 경우, 이동을 건너뜀
        if stone_x + dx > 8 or stone_y + dy > 8 or stone_x + dx < 1 or stone_y + dy < 1:
            continue
        else:
            stone_x += dx
            stone_y += dy

    # 킹의 위치 업데이트
    king_x, king_y = nx, ny
            

print(chr(king_x + 64) + str(king_y))
print(chr(stone_x + 64) + str(stone_y))