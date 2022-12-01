def solution(dirs):
    
    answer = 0

    # 명령어별 이동
    dir = {"U": (0,1), "D": (0,-1), "L": (-1,0), "R": (1,0)}

    # 이동 좌표 기록하는 배열
    path = []

    # 초기 좌표(0,0)
    x, y = 0, 0

    for d in dirs:
        # 명령에 의한 이동 방향
        dx, dy = dir[d]

        # 이동할 좌표
        nx, ny = x + dx, y + dy

        # 좌표평면의 경계를 넘어 가는 경우
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        
        # 이미 거쳐 간 길이라면 좌표는 이동하고 길이 측정은 안 함
        if (x, y, nx, ny) in path or (nx, ny, x, y) in path:
            x, y = nx, ny
            continue

        # 경로에 이동 좌표 및 방향 저장
        path.append((x, y, nx, ny))
        path.append((nx, ny, x, y))

        # 새로운 좌표로 현재 좌표 업데이트
        x, y = nx, ny

        # 처음 걸어본 거리 증가
        answer += 1

    return answer