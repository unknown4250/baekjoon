def solution(survey, choices):
    
    answer = ''

    # 성격 유형별 점수
    personalities = {"R":0, "T":0, "C":0, "F":0, 
                     "J":0, "M":0, "A":0, "N":0 }

    # 선택지에 따라 점수를 획득하는 유형과 획득하는 점수
    scores = [(0,0),(0,3),(0,2),(0,1),(0,0),(1,1),(1,2),(1,3)]

    for i in range(len(survey)):
        idx, score = scores[choices[i]]
        personalities[survey[i][idx]] += score

    # R, T 유형 선택 -> 점수 같으면 R 선택됨
    if personalities['R'] >= personalities['T']:
        answer += 'R'
    else:
        answer += 'T'

    # C, F 유형 선택 -> 점수 같으면 C 선택됨
    if personalities['C'] >= personalities['F']:
        answer += 'C'
    else:
        answer += 'F'

    # J, M 유형 선택 -> 점수 같으면 J 선택됨
    if personalities['J'] >= personalities['M']:
        answer += 'J'
    else:
        answer += 'M'

    # A, N 유형 선택 -> 점수 같으면 A 선택됨    
    if personalities['A'] >= personalities['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer