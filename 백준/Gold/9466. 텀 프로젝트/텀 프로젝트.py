import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

t = int(input())    # 테스트케이스 수

def dfs(x):
    global result

    visited[x] = True   # 방문 표시
    cycle.append(x)     # 탐색 경로 추가

    # 다음으로 탐색할 노드 
    cur = students[x]

    # 방문했던 곳이면 팀을 이루는지 확인
    if visited[cur]:
        # 탐색했던 경로에 현재 노드있는지 확인 -> 사이클 형성 여부 확인
        if cur in cycle:
            # 사이클이 되는 부분부터만 팀을 이룸
            result += cycle[cycle.index(cur):]
        return
    else:
        dfs(cur)

for _ in range(t):
    # 학생 수 입력
    n = int(input())
    # 선택 결과 입력
    students = [0] + list(map(int, input().split()))

    # 방문 확인
    visited = [False] * (n+1)   

    # 팀이 된 학생 목록
    result = [] 

    # 1번부터 n번 학생까지 탐색
    for i in range(1, n+1):
        # 방문하지 않았던 학생만 탐색
        if not visited[i]:
            # 해당 학생의 탐색 경로를 저장
            cycle = []
            dfs(i)

    # (전체 학생 수) - (팀을 이룬 학생 수)
    print(n - len(result))