import copy
import sys
input = sys.stdin.readline

fishes = [[] for _ in range(4)]

# 최종 결과
answer = 0

# 물고기 정보 입력
for i in range(4):
    lst = list(map(int, input().split()))

    # 물고기 번호, 방향 입력
    fishes[i].append([lst[0],lst[1]-1])
    fishes[i].append([lst[2],lst[3]-1])
    fishes[i].append([lst[4],lst[5]-1])
    fishes[i].append([lst[6],lst[7]-1])


# 물고기 번호에 따른 이동 방향
#  1(↑), 2(↖), 3(←), 4(↙), 5(↓), 6(↘), 7(→), 8(↗)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def dfs(arr, shark_x, shark_y, total):
    global answer

    # 해당 위치의 물고기 먹기
    total += arr[shark_x][shark_y][0]

    # 상어가 먹은 물고기의 최대값 구하기
    answer = max(answer, total)

    # 먹을 수 없는 물고기로 표시
    arr[shark_x][shark_y][0] = 0


    # 1번부터 16번까지의 모든 물고기 이동시키기
    for i in range(1, 17):
        fish_x, fish_y = -1, -1

        # 현재 물고기의 위치 찾기
        for x in range(4):
            for y in range(4):
                if arr[x][y][0] == i:
                    fish_x, fish_y = x, y
                    break
        
        # 물고기 위치 찾을 수 없으면 pass
        if fish_x == -1 and fish_y == -1:
            continue
        
        # 현재 물고기의 방향
        fish_dir = arr[fish_x][fish_y][1]

        # 물고기가 이동할 위치 찾기
        for j in range(8):
            # 왼쪽 45도로 회전
            nd = (fish_dir+j) % 8

            # 방향에 따라 이동할 새로운 위치
            nx = fish_x + dx[nd]
            ny = fish_y + dy[nd]

            # 공간의 경계 밖이거나 이동할 위치에 상어가 있으면 건너뜀
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or (nx == shark_x and ny == shark_y):
                continue
        
            # 이동한 방향으로 방향 변경
            arr[fish_x][fish_y][1] = nd
            # 이동한 위치에 있던 물고기와 현재 물고기의 위치,방향 정보 맞교환
            arr[fish_x][fish_y], arr[nx][ny] = arr[nx][ny], arr[fish_x][fish_y]
            break
    
    # 현재 상어 방향
    shark_dir = arr[shark_x][shark_y][1]
    
    # 현재 상어의 위치에서 먹을 수 있는 물고기들 확인
    for i in range(1, 5):
        # 같은 방향으로 i칸만큼 이동
        nx = shark_x + dx[shark_dir]*i
        ny = shark_y + dy[shark_dir]*i

        # 상어가 이동 가능한 위치(=먹을 수 있는 물고기의 위치) 찾기
        if nx >= 0 and nx < 4 and ny >= 0 and ny < 4:
            # 해당 위치에 물고기가 있는지 확인
            if arr[nx][ny][0] > 0:
                # 이동 가능한 위치에 대해 dfs 재귀적 수행
                # 물고기의 위치, 방향 정보를 통째로 복사
                dfs(copy.deepcopy(arr), nx, ny, total)
            
dfs(fishes, 0, 0, 0)
print(answer)