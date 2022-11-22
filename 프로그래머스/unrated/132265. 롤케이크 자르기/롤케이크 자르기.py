from collections import Counter

def solution(topping):
    answer = 0

    # 모든 토핑의 개수 저장
    counter = Counter(topping)

    # 철수가 모든 토핑을 가진 상태에서 시작
    cheolsu = set(topping)

    # 동생은 하나의 토핑도 없는 상태에서 시작
    brother = set()

    # 철수가 동생에게 토핑 하나씩 줌
    for elem in topping:
        # 동생의 토핑 증가
        brother.add(elem)

        # 해당 토핑 개수 감소
        counter[elem] -= 1

        # 해당 토핑의 개수가 0 이하면, 철수에게 그 토핑은 없어짐
        if counter[elem] <= 0:
            cheolsu.remove(elem)
        
        # 두 사람이 가진 토핑 종류 개수가 같으면 +1
        if len(cheolsu) == len(brother):
            answer += 1

    return answer