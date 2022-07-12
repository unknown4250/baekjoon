n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = 0

# a 배열은 오름차순, b 배열은 내림차순으로 정렬해서 곱하기
for i in range(n):

    # a 배열의 최소값
    a_min = min(a)

    # b 배열을 정렬하면 안되므로 max 함수로 최대값 찾기
    b_max = max(b)

    s += a_min * b_max

    # 계산에 사용한 각각의 최소값과 최대값은 배열에서 제거
    a.pop(a.index(a_min))
    b.pop(b.index(b_max))

print(s)