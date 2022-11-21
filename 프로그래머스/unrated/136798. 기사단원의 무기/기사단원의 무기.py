def solution(number, limit, power):
    
    answer = 0
    
    # 약수 구하는 함수
    def divisors(num):
        count = 0
        
        # 1부터 입력 값의 제곱근까지 탐색
        for i in range(1, int(num**(1/2)) + 1):
            # 나머지가 0이면 약수
            if num % i == 0:
                count += 1
                
                # 약수의 제곱 값이 num이 아니면,
                # 해당 약수와 짝이 되는 약수가 더 존재하므로 약수 개수 +1
                if i ** 2 != num:
                    count += 1
                    
            # 약수 개수가 제한 수치보다 큰 경우, power로 값 제한
            if count > limit:
                return power
                
        return count


    for i in range(1, number+1):
        answer += divisors(i)

    return answer
