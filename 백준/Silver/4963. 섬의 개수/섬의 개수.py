import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x < 0 or x >= h or y < 0  or y >= w or graph[x][y] != 1:
        return
        
    graph[x][y] = 0
    
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    dfs(x-1, y-1)
    dfs(x+1, y-1)
    dfs(x-1, y+1)
    dfs(x+1, y+1)
    

while True:
    w, h = map(int, read().split())

    if w == 0 and h == 0: break
    
    graph = []

    islands_num = 0
    
    for _ in range(h):
        graph.append(list(map(int, read().split())))
    
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                islands_num += 1
  
    print(islands_num)