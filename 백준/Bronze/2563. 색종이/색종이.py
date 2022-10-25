import sys
input = sys.stdin.readline

n = int(input())

papers = [[0] * 101 for _ in range(101)]

for _ in range(n):
    x, y = map(int, input().split())
    
    for i in range(x, x + 10):
        for j in range(100-y, 100-(y+10), -1):
            papers[i][j] = 1

cnt = 0

for i in range(1, 101):
    for j in range(1, 101):
        if papers[i][j] == 1:
            cnt += 1
print(cnt)