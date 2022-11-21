def solution(k, ranges):
    answer = []

    # 우박수열에 의해 생기는 좌표
    coordinates = []
    
    while True:
        # 좌표 배열에 추가
        coordinates.append(k)

        # k 값이 1이 되면 종료
        if k == 1:
            break
        
        # 짝수면 2로 나누기
        if k % 2 == 0:
            k //= 2
        
        # 홀수면 3 곱하고 1 더하기
        else:
            k = k * 3 + 1


    # x, y는 각각 시작과 끝에서 떨어진 값(offset)
    for x, y in ranges:

        end = len(coordinates) + y - 1

        # 좌측 x좌표가 우측 y좌표보다 큰 경우
        if x > end:
            answer.append(-1)
        else:
            tmp = 0
            # 각 구간의 정적분 결과를 누적해서 더함
            for i in range(x, end):
                # 정적분 결과 = 사다리꼴 넓이
                tmp += (coordinates[i] + coordinates[i+1]) / 2
            answer.append(tmp)

    return answer