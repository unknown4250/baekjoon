import sys
input = sys.stdin.readline

n, m = map(int, input().split())

not_listened = {input() for _ in range(n)}
    
res = []
for _ in range(m):
    name = input()
    if name in not_listened:
        res.append(name)

res.sort()
print(len(res))
print("".join(res))