from collections import deque

def solution(numbers, target):
    answer = 0

    queue = deque()
    n = len(numbers)

    # 입력 배열의 첫번째 값 저장
    queue.append((numbers[0], 0))    
    queue.append((-1 * numbers[0], 0))

    # 배열의 모든 원소를 방문 
    while queue:
        num, idx = queue.popleft()

        # 인덱스 증가
        idx += 1
        
        # 배열의 마지막 값이 아니면 원소 값을 더하거나 빼서 배열에 추가
        if idx < n:
            queue.append((num + numbers[idx], idx))
            queue.append((num - numbers[idx], idx))

        # 배열 원소를 다 방문했다면
        else:
            # 계산 결과가 target과 같다면 경우의 수 증가
            if num == target:
                answer += 1

    return answer