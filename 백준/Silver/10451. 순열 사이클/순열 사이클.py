import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x, start):
    global answer
    
    # x가 가리키는 정점
    next = numbers[x]

    # 해당 정점에 방문했던 경우
    if visited[next]:
        # 해당 정점과 시작점이 같다면 사이클 + 1
        if start == next:
            answer += 1
        return
    # 처음 방문하는 경우
    else:
        # 방문 표시
        visited[next] = True
        # 연결된 정점이 사이클 형성하는지 확인하기 위해  dfs 수행
        dfs(next, start)



# 테스트케이스 개수
t = int(input())

for _ in range(t):
    # 순열의 크기
    n = int(input())

    # 순열 입력
    numbers = [0] + list(map(int, input().split()))

    # 정점의 방문 표시
    visited = [True] + [False] * n

    # 사이클 개수
    answer = 0

    for i in range(1, n+1):
        # 방문하지 않은 정점이라면
        if not visited[i]:
            # 방문 표시
            visited[i] = True
            # dfs 수행
            dfs(i, i)

    print(answer)