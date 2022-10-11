from collections import deque
import sys
sys.setrecursionlimit(10**6)

def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(0,0)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m or maps[nx][ny] != 1:
                continue

            maps[nx][ny] = maps[x][y] + 1
            queue.append((nx, ny))
    
    answer = maps[-1][-1]
    return answer if answer > 1 else -1