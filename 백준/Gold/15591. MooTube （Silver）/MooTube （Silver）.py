import collections
import sys
input = sys.stdin.readline

n, q = map(int, input().split())

graph = collections.defaultdict(list)

# 그래프 구축
for _ in range(n-1):
    a, b, u = map(int, input().split())
    graph[a].append((b, u))
    graph[b].append((a, u))

# v번 동영상을 시작점으로 탐색해야 함
# 즉, 매 질문마다 유사도 계산 필요
for _ in range(q):
    k, v = map(int, input().split())
    queue = []
    # 초기 유사도는 0이 아닌 무한대 값으로 설정 (최소값으로 갱신해야 하므로)
    queue.append((v, int(1e9)))

    # 방문 여부 체크할 배열
    visited = [False] * (n + 1)
    # 시작점(v번 동영상) 방문 체크
    visited[v] = True

    cnt = 0

    while queue:
        cur_video, cur_usado = queue.pop()

        # 인접한 동영상 탐색
        for next_video, next_usado in graph[cur_video]:
            # 더 낮은 유사도 선택
            usado = min(cur_usado, next_usado)

            # 방문하지 않았고, 유사도가 k 이상인 인접 동영상 카운트
            if usado >= k and (not visited[next_video]):
                cnt += 1    # 추천 가능한 동영상이므로 개수 추가
                visited[next_video] = True  # 방문 표시
                # 현재 동영상에 인접한 동영상을 탐색하기 위해 배열에 추가
                queue.append((next_video, usado))
    
    print(cnt)