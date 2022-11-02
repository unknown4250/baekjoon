import sys
input = sys.stdin.readline

n = int(input())

# 퀸을 놓는 방법의 수
result = 0

# 인덱스 = 행 번호, 배열 값 = 열 번호
graph = [0 for _ in range(n)]

# 체스판 탐색 여부
visited = [0] * n

# 대각선에 퀸이 있는지 확인
def check(x):
    for i in range(x):
        # row끼리의 차이와 열끼리의 차이의 절대 값이 같다면 대각선 위치에 있음
        if abs(graph[x]-graph[i]) == x - i:
            return False
    return True

def dfs(x):
    global result
    
    # n번째 퀸을 놓은 경우
    if x == n:
        result += 1     # 방법 개수 1 추가
        return          # 탐색 종료
    
    # 모든 체스판의 row 확인
    for i in range(n):
        if not visited[i]:
            graph[x] = i # (x, i)에 퀸 놓기
            
            # 대각선에 퀸이 있는지 확인
            if check(x):
                visited[i] = True # 퀸 놓기
                dfs(x+1) # 퀸을 놓을 수 있는 행 찾기
                visited[i] = False # 퀸을 n개 놓을 수 없으면 퀸을 놓지 않도록 초기화
        
dfs(0)
print(result)