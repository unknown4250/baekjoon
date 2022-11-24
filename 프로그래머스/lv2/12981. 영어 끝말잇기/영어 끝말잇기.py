def solution(n, words):
    # 단어 등장 여부 확인
    counter = {}
    # 플레이어별 참여 횟수 저장
    player = {i:0 for i in range(1, n+1)}

    num = 1
    for i in range(len(words)):
        # 해당 플레이어의 참여 횟수 증가
        player[num] += 1

        # 이전에 나온 단어면 탈락
        if counter and words[i] in counter:
            return [num, player[num]]

        # 직전의 단어 끝자리와 현재 단어의 첫 글자가 다르면 탈락
        if i > 0 and words[i-1][-1] != words[i][0]:
            return [num, player[num]]
        
        # 단어 사용 여부 기록
        counter[words[i]] = 1

        # n번째 사람이었다면 1번째로 순서 돌아감
        if num % n == 0:
            num = 1
        else:
            num += 1

    # 탈락자가 없으면 [0,0] 리턴
    return [0,0]
