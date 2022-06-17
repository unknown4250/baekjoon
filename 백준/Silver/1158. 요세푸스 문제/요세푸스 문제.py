import sys
input = sys.stdin.readline


n, k = map(int, input().split())

nums = [i for i in range(1, n+1)]
idx, res = 0, []

for i in range(n):
    idx = (idx + k - 1) % len(nums)
    res.append(str(nums[idx]))
    nums.pop(idx)

print('<' + ', '.join(list(map(str, res))) + '>')