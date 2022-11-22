from collections import deque

def solution(order):
    answer = 0
    
    # 기존 컨테이너
    origin_container = deque([i for i in range(1, len(order)+1)])

    # 보조 컨테이너
    sub_container = []

    idx = 0

    while True:
        # 옮겨야 될 상자가 기존 컨테이너 벨트의 맨 앞 상자인 경우
        if origin_container and order and order[idx] == origin_container[0]:
            origin_container.popleft() # 기존 컨테이너에서 해당 상자 제거
            answer += 1 # 옮길 수 있는 상자 개수 + 1
            idx += 1    # 다음 배달 순서로 이동

        # 옮겨야 될 상자가 서브 컨테이너의 마지막 상자인 경우 
        elif sub_container and order and order[idx] == sub_container[-1]:
            sub_container.pop() # 서브 컨테이너에서 해당 상자 제거
            answer += 1 # 옮길 수 있는 상자 개수 + 1
            idx += 1    # 다음 배달 순서로 이동

        # 기존 컨테이너에서 서브 컨테이너로 상자를 옮기기
        elif origin_container:
            sub_container.append(origin_container.popleft())
        
        # 더이상 상자를 실을 수 없는 경우
        else:
            break

    return answer