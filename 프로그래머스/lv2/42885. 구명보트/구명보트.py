from collections import deque
def solution(people, limit):
    answer = 0

    # 손님들의 무게를 정렬해서 데크에 저장
    people = deque(sorted(people))

    while people:
        # 마지막에 남는 사람이 있다면 구명보트 + 1
        if len(people) == 1:
            answer += 1
            break

        # 최소, 최대 몸무게를 가진 2명이 limit이 넘는 경우
        if people[0] + people[-1] > limit:
            # 최대 몸무게의 사람만 제거(혼자 구명보트에 탑승해야 함)
            people.pop()
        # 2명을 함께 구출하는 경우
        else:
            # 최소 몸무게 가진 사람 제외
            people.popleft()
            # 최대 몸무게 가진 사람 제외
            people.pop()

        # 구명보트 개수 증가
        answer += 1
    
    return answer 