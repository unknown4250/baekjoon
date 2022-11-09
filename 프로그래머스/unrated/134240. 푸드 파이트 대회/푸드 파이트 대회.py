def solution(food):
    answer = ''
    
    for i in range(1, len(food)):
        # 음식 개수가 홀수면, 한개 더 적게 사용
        if food[i] % 2 == 1:
            food[i] -= 1
        
        # 두 선수가 음식을 반씩 나눠 먹음
        food[i] /= 2
        
        # 음식 양의 절반만큼 반복해서 음식을 배치함
        while food[i] > 0:
            answer += str(i)
            food[i] -= 1
            
    return answer + '0' + answer[::-1]