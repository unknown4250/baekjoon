hour, min = map(int, input().split())
extra_time = int(input())

extra_hour, extra_min = extra_time // 60, extra_time % 60

hour += extra_hour
min += extra_min

if min > 59:
   min -= 60
   hour += 1

if hour > 23:
    hour -= 24
    
print(hour, min)