answer = 0

def dfs(k, depth, dungeons, visited):
    global answer

    # 방문 가능한 최대 던전 수 찾기
    if depth > answer:
        answer = depth

    for i in range(len(dungeons)):
        # 방문하지 않은 던전이면서, 최소 필요 피로도보다 남은 피로도가 크면 방문 가능
        if not visited[i] and k >= dungeons[i][0]:
            # 방문 표시
            visited[i] = True

            # 현재 던전을 방문하고나서 그 이후의 탐험
            dfs(k-dungeons[i][1], depth+1, dungeons, visited)
            
            # 방문해보고 안되면 방문 취소
            visited[i] = False

def solution(k, dungeons):
    global answer

    # 방문 여부 표시할 배열
    visited = [False] * len(dungeons)

    # dfs 수행
    dfs(k, 0, dungeons, visited)

    return answer