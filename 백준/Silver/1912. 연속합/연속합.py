import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

for i in range(1, n):
    if nums[i] + nums[i-1] > 0:
        nums[i] = max(nums[i-1] + nums[i], nums[i])

print(max(nums))