def solution(n, times):
    answer = 0

    left, right = min(times), max(times) * n

    while left <= right:
        mid = (left + right) // 2

        checked = 0
        for time in times:
            # mid 분 동안 각 심사관이 심사할 수 있는 사람의 수
            checked += mid // time
            # 모든 심사관을 안 거쳐도 mid분 동안 n명 이상을 심사할 수 있다면 종료
            if checked >= n:
                break
                
        # 심사한 사람의 수 >= 심사받아야 할 사람의 수 : 최대 심사 시간을 줄임
        if checked >= n:
            answer = mid
            right = mid - 1
        # 심사한 사람의 수 < 심사받아야 할 사람의 수 : 최소 심사 시간을 늘림    
        else:
            left = mid + 1

    return answer
