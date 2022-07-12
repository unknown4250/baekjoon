import heapq

n = int(input())

nums = []

# 효율성을 위해 우선순위 큐 사용
for _ in range(n):
    heapq.heappush(nums, int(input()))

res = 0

for _ in range(n-1
    # heappop으로 작은 값 2개 꺼내서 더해주기
    sum = heapq.heappop(nums) + heapq.heappop(nums)
    res += sum

    # 이전 카드 묶음 합을 저장
    heapq.heappush(nums, sum)

print(res)
