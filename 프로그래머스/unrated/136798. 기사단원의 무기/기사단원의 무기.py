def solution(number, limit, power):
    
    answer = 1

    def divisors(num):
        count = 0

        for i in range(1, int(num**(1/2)) + 1):
            if num % i == 0:
                count += 1

                if i ** 2 != num:
                    count += 1

            if count > limit:
                return power
                
        return count


    for i in range(2, number+1):
        answer += divisors(i)

    return answer