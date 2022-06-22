import sys
input = sys.stdin.readline

n = int(input())

arr = [0]
for _ in range(n):
    arr.append(int(input()))

if n == 1:
    print(arr[1])
else:
    dp = [0] * (n + 1)
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]

    for i in range(3, n+1):
        # 현재 위치에서 선택해야 할 값 : "1칸 밑의 점수 + 3칸 밑까지의 올라오는 최대 점수"와 "2칸 밑까지의 점수" 중 최대값
        dp[i] += max(dp[i-3]+arr[i-1], dp[i-2]) + arr[i] 
    
    print(dp[n])