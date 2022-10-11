def solution(n, computers):
    def dfs(x):
        if visited[x]:
            return
        
        visited[x] = True
        for i in range(len(computers[x])):
            # 연결된 컴퓨터라면 dfs 계속 수행
            if computers[x][i] == 1:
                dfs(i)

    answer = 0
    visited = [False] * n
    for i in range(n):
        # 방문하지 않은 노드에 대해서만 dfs 수행
        if not visited[i]:
            dfs(i)
            answer += 1

    return answer