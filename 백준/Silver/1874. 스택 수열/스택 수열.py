import sys
input = sys.stdin.readline


n = int(input())

stack, res = [], []
cnt = 0
top = False

for _ in range(n):
    num = int(input())
    
    while cnt < num:
        cnt += 1
        stack.append(cnt)
        res.append("+")
    
    if stack[-1] == num:
        stack.pop()
        res.append("-")
    else:
        print("NO")
        top = True
        break

if not top:
    for i in res:
        print(i)