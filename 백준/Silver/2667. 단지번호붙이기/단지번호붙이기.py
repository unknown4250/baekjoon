from itertools import count
import sys
read = sys.stdin.readline

n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x < 0 or x >= n or y < 0  or y >= n or graph[x][y] != 1:
        return False
    
    global count
    # 같은 단지에 속하는 집 개수
    count += 1

    # 중복 탐색하지 않도록 현재 위치를 0으로 변경
    graph[x][y] = 0

    # 현재 위치를 기준으로 상하좌우 집 탐색
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)

    return True
    
count = 0 # 단지별 집의 수
result = 0 # 총 단지 수
num = []
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            num.append(count)
            count = 0
            result += 1

num.sort() # 단지별 집의 수 오름차순 정렬
print(result)
print("\n".join(list(map(str, num))))