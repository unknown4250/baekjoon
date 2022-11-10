def solution(a, b, n):
    answer = 0
    
    while n // a >= 1:
        answer += (n // a) * b # 새로 받아온 콜라의 개수
        n = n - (a * (n // a)) + (n // a) * b  # 가져간만큼 빈병 개수 차감, 받아온 콜라 병 추가
        print(answer, n)
    return answer
