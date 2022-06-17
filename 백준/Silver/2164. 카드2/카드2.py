import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
deque = deque()

for i in range(n): 
    deque.append(i+1)

while len(deque) > 1:
    deque.popleft()
    deque.append(deque.popleft())

print(deque.pop())