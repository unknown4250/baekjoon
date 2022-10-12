
import sys
input = sys.stdin.readline

n = int(input())
own_card = {i for i in list(map(int, input().split()))}
m = int(input())
check_card = [i for i in list(map(int, input().split()))]

res = []
for num in check_card:
    if num in own_card:
        res.append("1")
    else:
        res.append("0")

print(" ".join(res))