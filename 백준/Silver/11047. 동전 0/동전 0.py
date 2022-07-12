import sys

n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

res = 0
for i in range(n-1, -1, -1):
    if k >= coins[i]:
        res += k // coins[i]
        k %= coins[i]

        if k <= 0:
            break

print(res)