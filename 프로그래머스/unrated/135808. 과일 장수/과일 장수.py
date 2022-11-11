def solution(k, m, score):
    # 결과 값
    answer = 0

    # 점수들을 내림차순 정렬
    score.sort(reverse=True)
    
    # 하나의 상자
    tmp = []

    for i in range(len(score)):
        # 사과를 상자에 넣기
        tmp.append(score[i])

        # m개의 사과를 상자에 넣었다면
        if (i + 1) % m == 0:
            # 상자 하나의 이익 : 최저 사과 점수 x 한 상자에 담긴 사과 개수
            answer += min(tmp) * m
            # 사과들을 새로 담기 위해 초기화
            tmp.clear()
    return answer