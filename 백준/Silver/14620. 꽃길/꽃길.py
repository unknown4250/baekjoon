import sys
input = sys.stdin.readline

n = int(input())

prices = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = int(1e9)

# 방문한 위치인지 확인
def check(i, j, visited):
    # 씨앗을 기준으로 꽃잎들의 위치 탐색
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]

        # 해당 위치를 방문했다면 False 리턴
        if (nx, ny) in visited:
            return False
    # 방문하지 않았다면 True 리턴
    return True


def dfs(visited, total):
    global answer
    
    # 이전 최소비용보다 현재 비용이 크면 비교 안함
    if total >= answer:
        return
    
    # 3가지 꽃을 겹치지 않고 놓은 경우
    if len(visited) == 15:
        # 최소 비용인지 비교
        answer = min(answer, total)
    else:
        # 씨앗의 가능한 위치: 상하좌우로부터 한 칸씩 떨어져야 함
        for i in range(1, n-1):
            for j in range(1, n-1):
                # 해당 위치를 방문한적 없고, 꽃이 필 수 있는 위치인지 확인
                if (i, j) not in visited and check(i, j, visited):
                    # 현재 위치를 기준으로 씨앗을 심고 꽃잎을 넣을 수 있는지 확인
                    cur = [(i, j)]   # 현재 위치(씨앗) 방문 처리
                    cur_cost = prices[i][j] # 씨앗 위치의 비용 추가
                    
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        cur.append((nx, ny))    # 현재 위치(꽃잎) 방문 처리
                        cur_cost += prices[nx][ny]  # 꽃잎 위치의 비용 추가

                    # 탐색 수행
                    dfs(visited + cur, total + cur_cost)

dfs([], 0)
print(answer)
