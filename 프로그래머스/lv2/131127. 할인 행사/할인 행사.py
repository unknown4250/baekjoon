from collections import Counter

def solution(want, number, discount):
    answer = 0

    dict = {}

    # 해시 테이블(key: 상품, value: 수량) 구축
    for i in range(len(want)):
        dict[want[i]] = number[i]

    for i in range(len(discount)-9):
        # 현재부터 10일 동안의 상품 종류와 수량이 같은 경우
        if dict == Counter(discount[i:i+10]):
            # 회원 가입 가능한 날짜 증가
            answer += 1

    return answer