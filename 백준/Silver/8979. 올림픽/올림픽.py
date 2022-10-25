from sys import stdin
input = stdin.readline

n, k = map(int, input().split())

# 국가 번호, 금, 은, 동메달 순서대로 저장
medals = [list(map(int, input().split())) for _ in range(n)]

# 메달별 개수 많은 순(내림차순) 정렬
medals.sort(key=lambda x:(-x[1], -x[2], -x[3]))

idx = -1

# k 국가의 인덱스 찾기
for i in range(n):
    if medals[i][0] == k:
        idx = i
        break
rank = 1

for num, g, s, b in medals:
    if g > medals[idx][1]:
        rank += 1

    elif g == medals[idx][1] and s > medals[idx][2]:
        rank += 1

    elif g == medals[idx][1] and s == medals[idx][2] and b > medals[idx][3]:
        rank += 1

print(rank)