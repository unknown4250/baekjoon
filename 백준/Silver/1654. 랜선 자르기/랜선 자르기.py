import sys
read = sys.stdin.readline

k, n = map(int, read().split())

cables = []
for _ in range(k):
    cables.append(int(read()))


left, right = 1, max(cables)
answer = 0
while left <= right:
    mid = (left + right) // 2
    
    total = 0
    for cable in cables:
        total += cable // mid

    # 최대 길이를 찾아야 하므로 upper bound를 사용해야 한다.
    # 198, 199, 200 모두 n이 11개이기 때문이다.
    # upper bound를 사용한다는 것은 mid 길이로 잘랐을 때의 개수가 n보다 작다면
    # 자르고자 하는 길이를 줄이기 위해 최대 길이를 줄인다는 의미이다.
    # 크거나 같다면 최소 길이를 늘려야 한다.
    if total < n:
        right = mid - 1
    else:
        left = mid + 1

print(right)