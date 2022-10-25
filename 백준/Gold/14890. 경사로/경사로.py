import sys
input = sys.stdin.readline

n, l = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

def check(line):
    for i in range(1, n):
        # 낮은 칸과 높은 칸의 높이 차가 1보다 클 경우
        if abs(line[i] - line[i-1]) > 1:
            return False
        
        # 현재 위치 기준으로 오른쪽에 경사로가 위치함
        if line[i] < line[i-1]:
            for j in range(l):
                # 아래 3가지 경우는 경사로를 놓을 수 없음
                # 1. 경사로가 지도를 벗어날 경우
                # 2. 낮은 지점의 칸이 L개가 연속되지 않은 경우
                # 3. 이미 경사로가 놓인 경우
                if i + j >= n or line[i] != line[i+j] or visited[i+j]:
                    return False

                # 경사로 위치 표시
                if line[i] == line[i+j]:
                    visited[i+j] = True

        # 현재 위치 기준으로 왼쪽에 경사로가 위치함
        elif line[i] > line[i-1]:
            for j in range(l):
                if i - j - 1 < 0 or line[i-1] != line[i-j-1] or visited[i-j-1]:
                    return False
                if line[i-1] == line[i-j-1]:
                    visited[i-j-1] = True
    return True
        

# 가로 방향 확인
for i in range(n):
    visited = [False] * n
    if check([map[i][j] for j in range(n)]):
        cnt += 1

# 세로 방향 확인
for i in range(n):
    visited = [False] * n
    if check([map[j][i] for j in range(n)]):
        cnt += 1

print(cnt)