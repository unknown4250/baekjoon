def solution(X, Y):
    answer = []
    
    x_dict, y_dict = {}, {}
    
    # X, Y에 포함된 정수들의 개수 카운트
    for x in X:
        x_dict[x] = x_dict.get(x, 0) + 1
    
    for y in Y:
        y_dict[y] = y_dict.get(y, 0) + 1
    
    # X를 기준으로 Y와의 짝꿍 탐색
    for k, v in x_dict.items():
        # X에 있는 정수가 Y에도 있는 경우
        if k in y_dict:
            # X, Y에 공통된 개수만큼 결과 배열에 추가
            while y_dict[k] > 0 and x_dict[k] > 0:
                answer.append(k)
                y_dict[k] -= 1
                x_dict[k] -= 1
                
    # 짝꿍이 없을 경우
    if not answer:
        return "-1"
    
    # 모든 짝꿍이 '0'일 경우, 0 리턴
    if answer.count('0') == len(answer):
        return "0"
    
    # 가장 큰 정수를 리턴하기 위해 내림차순 정렬
    answer.sort(reverse=True)
    
    # 배열을 문자열로 리턴
    return "".join(answer)