import sys
input = sys.stdin.readline

arr = []
for _ in range(5):
    arr.append(input().strip())

for i in range(max(len(w) for w in arr)):
    for j in range(5):
        if i < len(arr[j]):
            print(arr[j][i], end='')