num = int(input())
answer = 0

for i in range(1, num+1):
    num_list = list(map(int, str(i)))
    
    if i < 100: answer += 1
    elif num_list[1] - num_list[0] == num_list[2] - num_list[1]:
        answer += 1

print(answer)