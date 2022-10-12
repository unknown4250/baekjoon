def solution(distance, rocks, n):
    answer = 0
    rocks.sort() # 이분 탐색은 정렬된 상태에서 가능
    left, right = 0, distance

    while left <= right:
        # 거리의 최솟값을 범위의 중간 값으로 초기화
        mid = (left + right) // 2
        min_dist = float('inf')

        cur_idx = 0 # 현재 위치
        remove_cnt = 0 # 제거한 바위 개수

        for rock in rocks:
            # 바위와 현재 위치 사이의 거리
            diff = rock - cur_idx

            # mid보다 거리가 짧으면 바위를 제거
            if diff < mid:
                remove_cnt += 1
            # mid보다 거리가 길면 바위를 그대로 놔둠
            else:
                # 현재 위치를 바위의 위치로 변경
                cur_idx = rock
                # 최소 거리 업데이트
                min_dist = min(min_dist, diff)
        
        # mid 값 업데이트는 제거된 바위 개수가 기준이 됨
        if remove_cnt > n:
            # n보다 많이 줄였다면 mid를 줄이기
            right = mid - 1
        else:
            # n보다 적게 줄였다면 mid를 늘려서 바위 더 제거해야 함
            answer = min_dist
            left = mid + 1

    return answer