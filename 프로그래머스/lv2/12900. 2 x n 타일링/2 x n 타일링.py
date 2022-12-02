def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    answer = 0

    cnt1 = 1
    cnt2 = 2

    for i in range(n-2):
        answer = cnt1
        cnt1 = cnt2
        cnt2 = cnt1 + answer
    
    answer = cnt2 % 1000000007

    return answer