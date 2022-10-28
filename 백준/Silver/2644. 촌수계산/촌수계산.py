import collections
import sys
input = sys.stdin.readline

family = collections.defaultdict(list)

n = int(input())

# 촌수 계산해야 하는 서로 다른 두 사람의 번호
a, b = map(int, input().split())

m = int(input())

# 부모-자식 관계 입력
for _ in range(m):
    x, y = map(int, input().split())

    # 부모 자식간의 관계는 촌수가 같으므로 서로 연결됨
    family[x].append(y)
    family[y].append(x)

# 방문 여부 표시
visited = [False] * (n+1)

def bfs(start, end):

    # bfs 수행을 위한 큐 선언
    queue = collections.deque()

    # 시작점과 촌수(0) 입력
    queue.append((start,0))

    while queue:

        # 탐색할 번호, 촌수
        cur, depth = queue.popleft()

        # 계산해야 하는 사람 번호에 도달하면 탐색 종료
        if cur == end:
            print(depth) # 촌수 출력
            return

        # 친척 관계에 있는 사람 탐색
        for next in family[cur]:
            # 촌수 계산 안 한 사람만 탐색
            if not visited[next]:
                visited[next] = True
                # 직접 연결된 관계 아니라면 촌수 증가
                queue.append((next, depth+1))
    # 연결 관계 없으면 -1 출력
    print(-1)

bfs(a, b)