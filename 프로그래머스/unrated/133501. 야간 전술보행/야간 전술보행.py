def solution(distance, scope, times):

    # 화랑이가 움직일 수 있는 최대 거리로 초기화
    answer = distance

    for i in range(len(scope)):
        # 각 경비병의 감시 구간
        start, end = sorted(scope[i])

        # 각 경비병의 근무 시간, 휴식 시간
        work_time, rest_time = times[i]

        # 경비병의 감시 구간만 탐색
        while start <= end:
            # 현재 위치에서 경비병의 단위 시간(근무+휴식) 나누기
            status = start % (work_time + rest_time)

            # 경비병에게 발각되는 경우
            if status > 0 and status <= work_time:
                # 현재 위치(시간)를 저장
                answer = min(answer, start)
                break

            start += 1

    return answer