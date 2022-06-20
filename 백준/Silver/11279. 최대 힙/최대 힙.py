import sys
import heapq
input = sys.stdin.readline

max_heap = []

for _ in range(int(input())):
    n = int(input())

    if n == 0:
        if max_heap:
            print(abs(heapq.heappop(max_heap)))
        else:
            print(0)
    else:
        # heapq는 최소힙이고 + 음수가 입력되지 않는 가정이 있으므로
        # 입력 값을 음수로 바꾸면, 절대값이 클수록 힙의 상위에 위치하게 됨
        heapq.heappush(max_heap, -n)