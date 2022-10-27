import collections
import sys
input = sys.stdin.readline

n, m = int(input()), int(input())

friends = collections.defaultdict(list)

# 방문 여부
visited = [False] * (n+1)

# 친구 관계 정보 저장
for _ in range(m):
    a, b = map(int, input().split())
    # a와 b가 친구면 b와 a도 친구
    friends[a].append(b)
    friends[b].append(a)

# bfs 구현을 위한 큐
queue = collections.deque()

# 시작점(상근이)부터 탐색 시작
queue.append((1, 0))

# 시작점 방문 표시
visited[1] = True

# 초대할 친구의 수
cnt = 0

while queue:
    # 친구 혹은 친구의 친구인지 판별하기 위한 depth
    cur, depth = queue.popleft()

    # depth가 2 이하면 초대
    if depth < 3:
        cnt += 1

    # 연결된 친구 탐색
    for next in friends[cur]:
        # 방문하지 않았고 친구 혹은 친구의 친구라면
        if not visited[next]:
            queue.append((next, depth+1))
            visited[next] = True # 방문 표시

# 상근이 제외한 사람 수
print(cnt - 1)