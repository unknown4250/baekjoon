n = int(input())

rooms = []
for _ in range(n):
    rooms.append(list(map(int, input().split())))

# 끝나는 시간, 시작 시간 기준으로 정렬
rooms.sort(key= lambda x:(x[1], x[0]))

res = 1

# 가장 첫 번째 회의의 끝나는 시간으로 초기화
end_time = rooms[0][1]

for i in range(1, n):
    # 회의 끝나는 시간이 다른 회의 시작 시간보다 전에 끝나는 경우 
    if end_time <= rooms[i][0]:
        # 회의실 하나 더 필요함
        res += 1
        end_time = rooms[i][1]
        
print(res)