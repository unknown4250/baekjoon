import sys
input = sys.stdin.readline


# 가로줄 확인
def check_row(x, n):
    for i in range(9):
        if sudoku[x][i] == n:
            return False
    return True

# 세로줄 확인
def check_column(y, n):
    for i in range(9):
        if sudoku[i][y] == n:
            return False
    return True

# 3x3 정사각형 확인
def check_square(x, y, n):
    # (x, y)가 속한 정사각형 범위
    nx = x // 3 * 3
    ny = y // 3 * 3

    for i in range(3):
        for j in range(3):
            if n == sudoku[nx+i][ny+j]:
                return False
    return True

# dfs + 백트래킹
def dfs(idx):
    # 스도쿠의 빈칸을 다 채웠다면
    if idx == len(blank):
        for i in range(9):
            # 한줄 씩 출력
            print(*sudoku[i])
        # 프로세스 종료
        exit(0)

    for i in range(1, 10):
        # 빈칸의 좌표
        x, y = blank[idx][0], blank[idx][1]

        if check_row(x, i) and check_column(y, i) and check_square(x, y, i):
            # 가로, 세로, 3x3 정사각형에 없는 숫자라면 빈칸에 채워넣음
            sudoku[x][y] = i
             # 다음 빈칸 탐색
            dfs(idx+1)
            # 초기화(정답 없을 경우 대비)
            sudoku[x][y] = 0

# 스도쿠판 입력
sudoku = [list(map(int, input().split())) for _ in range(9)]
blank = []

for i in range(9):
    for j in range(9):
        # 스도쿠 판에서 값이 0인 위치 표시
        if sudoku[i][j] == 0:
            blank.append((i,j))
dfs(0)