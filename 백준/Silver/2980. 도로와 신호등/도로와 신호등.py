from sys import stdin
input = stdin.readline

n, l = map(int, input().split())

# 총 걸린 시간
total_time = 0

# 시작 지점
prev = 0

for _ in range(n):
    d, r, g = map(int, input().split())
    
    # 총 시간 = 현재 신호등 위치 - 이전 신호등 위치
    total_time += d - prev
    
    # (빨간색 지속 시간 + 초록색 지속 시간)을 총 시간에서 나눈 나머지가
    # 빨간색 신호의 지속 시간보다 짧다면 그만큼 대기 시간이 발생함 
    if (total_time % (r + g)) < r:
        total_time += r - (total_time % (r + g))
    
    # 이전 신호등의 위치
    prev = d

# 마지막 신호등부터 도로 끝까지 이동하는데 소요되는 시간
total_time += l - d

print(total_time)