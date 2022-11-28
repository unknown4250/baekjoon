def solution(s):
    answer = []

    # 문자열의 튜플에서 숫자 부분만 저장
    src = s[2:-2].split("},{")

    # 각 튜플의 길이를 기준으로 정렬
    src.sort(key=lambda x: len(x))

    result = set()

    for nums in src:
        # 튜플의 숫자를 중복없이 저장
        tmp = set(list(map(int, nums.split(","))))
        
        # 이전 길이의 튜플과 중복되지 않은 원소만 결과 배열에 추가
        answer = answer + list(set.difference(tmp, result))
        
        # 이전 튜플 값 저장
        result = tmp
    
    return answer
    