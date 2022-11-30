def solution(msg):
    
    answer = []

    # 사전 초기화
    dictionary = {chr(i+65): i+1 for i in range(26)}

    # 다음에 들어올 단어의 색인 번호
    idx = 27

    # 단어의 처음과 끝 문자를 가리킬 포인터
    start, end = 0, 1

    while end < len(msg) + 1:

        # 검색할 단어
        word = msg[start:end]

        # 단어가 사전에 있는 경우
        if word in dictionary:
            # 다음 글자를 포함해서 재검색
            end += 1

        # 단어가 사전에 없는 경우
        else:
            # 이전 단어는 사전에 있으므로 현재의 마지막 문자를 제외하고 결과 배열에 추가
            answer.append(dictionary[word[:-1]])
            # 현재 단어의 색인 번호 부여
            dictionary[word] = idx
            # 색인 번호 증가
            idx += 1
            # 다시 탐색을 시작할 위치
            start = end - 1
    
    # 마지막으로 처리되지 않은 글자도 결과에 포함
    answer.append(dictionary[word])
        
    return answer