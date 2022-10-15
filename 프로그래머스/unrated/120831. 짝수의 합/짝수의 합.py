def solution(n):
    if n < 2:
        return 0
    
    answer = 0
    for i in range(2, n+1, 2):
        answer += i
    return answer