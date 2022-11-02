import sys
input = sys.stdin.readline

n = int(input())

# 능력치 정보 입력
graph = [list(map(int, input().split())) for _ in range(n)]

# True: 스타트팀, False: 링크팀
start_team = [False] * n

answer = int(1e9)

def dfs(depth, idx):
    global answer

    # 각 팀이 n/2명으로 나뉘었다면 능력치 비교
    if depth == n // 2:
        # 차이가 0이면 출력하고 바로 종료
        if answer == 0:
            print(answer)
            exit(0)

        # 스타트팀 능력치, 링크팀 능력치
        start_team_ability, link_team_ability = 0, 0

        # 팀원들의 능력치 합 구하기: S(i,j)와 S(j,i) 합산
        for i in range(n-1):
            for j in range(i+1, n):
                # 스타트팀인 경우
                if start_team[i] and start_team[j]:
                    start_team_ability += graph[i][j]
                    start_team_ability += graph[j][i]
                # 링크팀인 경우
                elif not start_team[i] and not start_team[j]:
                    link_team_ability += graph[i][j]
                    link_team_ability += graph[j][i]
        answer = min(answer, abs(start_team_ability-link_team_ability))
        return
    
    for i in range(idx, n):
        if not start_team[i]:
            start_team[i] = True
            dfs(depth+1, i+1)
            start_team[i] = False

dfs(0, 0)
print(answer)