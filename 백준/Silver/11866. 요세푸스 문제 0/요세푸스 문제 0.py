import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(range(1, n + 1))

idx = 0
res = []

while len(nums) > 0:
    idx = (idx + k - 1) % len(nums)
    res.append(nums.pop(idx))

print('<' + ', '.join(map(str, res)) + '>')