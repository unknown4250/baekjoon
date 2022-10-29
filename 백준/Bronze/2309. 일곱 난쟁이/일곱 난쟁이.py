import itertools
import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(9)]

"""
# 조합(itertools.combinations)을 사용한 풀이
# 난쟁이 중 7명을 조합
for i in itertools.combinations(arr, 7):
    # 해당 조합이 키의 합이 100인 경우
    if sum(i) == 100:
        # 정렬해서 출력
        for num in sorted(i):
            print(num)
        break
"""

# 완전 탐색 풀이
arr.sort()

# 입력된 9명 키의 합
heights = sum(arr)

for i in range(8):
    for j in range(i+1, 9):
        # 두 명의 키를 뺐을 때 100인 경우
        if heights - arr[i] - arr[j] == 100:
            for k in range(9):
                # 해당하는 두 위치(i, j) 제외하고 출력
                if k != i and k != j:
                    print(arr[k])
            exit()