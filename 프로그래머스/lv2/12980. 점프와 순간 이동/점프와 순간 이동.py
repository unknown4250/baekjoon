def solution(n):
    ans = 0
    
    while n:
        # n이 짝수이면, 순간 이동 가능
        if n % 2 == 0:
            n /= 2
        # n이 홀수이면, 짝수로 만들기 위해 한 칸만 이동
        else:
            n -= 1
            ans += 1

    return ans
