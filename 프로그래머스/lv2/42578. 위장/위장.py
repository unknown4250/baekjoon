def solution(clothes):
    hash = {}

    # 종류별로 옷이 몇 개 있는지 확인
    for name, type in clothes:
        # hash.get(type,0) : 해당 종류가 해시에 없다면 0을 반환
        hash[type] = hash.get(type, 0) + 1
    
    answer = 1

    # A(a)와 B(b, c)를 선택하는 경우의 수 : (A + 1) * (B + 1) = 2 * 3 = 6
    for type in hash:
        answer *= (hash[type] + 1)

    # 아무것도 입지 않는 경우는 제외
    return answer - 1