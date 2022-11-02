import sys
input = sys.stdin.readline

n, m = map(int, input().split())

answer = []


def backtracking(start):
    if len(answer) == m:
        print(*answer)
        return
    
    for i in range(start, n + 1):
        answer.append(i)
        backtracking(i)
        answer.pop()

backtracking(1)