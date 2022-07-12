import heapq

n = int(input())

nums = []
for _ in range(n):
    heapq.heappush(nums, int(input()))

res = 0

for _ in range(n-1):
    sum = heapq.heappop(nums) + heapq.heappop(nums)
    res += sum

    heapq.heappush(nums, sum)

print(res)