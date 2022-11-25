import math

def solution(n,a,b):
    answer = 0

    # 둘이 같은 경기라면 반복문 종료
    while a != b:

        # a, b를 2로 나누며 라운드 진출
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        
        # 라운드 증가
        answer += 1

        # 마지막 경기인 경우
        if a == 0 or b == 0:
            break
    
    return answer