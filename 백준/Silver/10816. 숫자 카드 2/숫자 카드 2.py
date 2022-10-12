import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
nums_counter = Counter(list(map(int, input().split())))
m = int(input())
nums_m = list(map(int, input().split()))

res = []
for i in range(m):
    if nums_m[i] in nums_counter:
        res.append(nums_counter[nums_m[i]])
    else:
        res.append(0)

print(" ".join(map(str, res)))