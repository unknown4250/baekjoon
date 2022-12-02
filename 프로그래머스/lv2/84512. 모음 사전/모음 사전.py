from itertools import product

def solution(word):

    words = []

    for i in range(1, 6):
        # 'A', 'E', 'I', 'O', 'U'로 중복 순열 만들기
        for p in product(['A','E','I','O','U'], repeat=i):
            words.append("".join(list(p)))

    # 생성한 순열 사전 순 정렬
    words.sort()

    # 입력 값의 인덱스 + 1
    return words.index(word) + 1