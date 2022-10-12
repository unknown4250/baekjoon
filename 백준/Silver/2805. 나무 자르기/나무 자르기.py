import sys
read = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

# 시간초과 나서 compare 함수 안에 작성함
# 아니면 pypy로 언어 설정 후 시도해볼 것
def compare(left, right):
    while left <= right:
        mid = (left + right) // 2
        total = 0

        for tree in trees:
            # 자르고 나무 길이가 남으면 더해야 함
            # 즉, 자르고 난 길이가 양수일 때만 더하기
            if tree - mid > 0:
                total += tree - mid

        # 자른 나무 길이의 합 >= m -> 자르는 위치가 낮으므로 높이 높여야 함
        if total >= m:
            left = mid + 1
        # 자른 나무 길이의 합 < m -> 자르는 위치가 높으므로 높이 낮춰야 함
        else:
            right = mid - 1

    return right

print(compare(1, max(trees)))