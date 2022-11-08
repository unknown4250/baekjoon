import heapq
import sys
input = sys.stdin.readline

n = int(input())

lessons = []

for _ in range(n):
    # 각 강의의 시작 시간과 종료 시간
    start, end = map(int, input().split())
    lessons.append([start, end])

# 시작 시간을 기준으로 정렬
lessons.sort()

# 강의실
room = []

# 첫 번째 강의 종료 시간을 큐에 삽입
heapq.heappush(room, lessons[0][1])

for i in range(1, n):
    # 이전 강의의 종료 시간보다 현재 강의의 시작 시간이 같거나 느린 경우
    if lessons[i][0] >= room[0]:
        # 같은 회의실에 이어서 배정 가능
        heapq.heappop(room) # 현재 종료 시간 제거
        heapq.heappush(room, lessons[i][1]) # 현재 강의를 새로운 종료 시간으로 업데이트
    else:
        # 이어서 배정하지 못하는 경우 = 새로운 강의실이 만들어지므로 room이 추가되는 것
        heapq.heappush(room, lessons[i][1])

# room의 길이 = 강의실 개수
print(len(room))