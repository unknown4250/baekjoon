def solution(citations):
    # 최대값을 구하기 위해 내림차순 정렬
    citations.sort(reverse=True)

    for i in range(len(citations)):
        # 논문 개수(h=i)가 인용수보다 크거나 작은 경우
        if citations[i] <= i:
            return i

    # 조건에 맞는 h 없는 경우, 가장 마지막 인덱스 리턴
    return len(citations)
