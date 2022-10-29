import itertools
import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(9)]

# 난쟁이 중 7명을 조합
for i in itertools.combinations(arr, 7):
    # 해당 조합이 키의 합이 100인 경우
    if sum(i) == 100:
        # 정렬해서 출력
        for num in sorted(i):
            print(num)
        break