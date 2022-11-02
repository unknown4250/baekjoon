import sys
input = sys.stdin.readline

l, c = list(map(int, input().split()))
letters = []

# 공백을 포함하지 않고 입력된 문자 저장
for ch in input().split( ):
    if ch != " ":
        letters.append(ch)

code = []

# 알파벳 사전순 정렬
letters.sort()

def backtracking(start):

    # 길이가 L인 암호가 완성되면 백트래킹 종료
    if len(code) == l:
        # 모음, 자음 개수
        vowel_num, consonant_num = 0, 0

        for i in range(l):
            # 모음
            if code[i] in ['a', 'e', 'i', 'o', 'u']:
                vowel_num += 1
            # 자음
            else:
                consonant_num += 1

        # 최소 1개의 모음, 최소 2개의 자음 포함
        if vowel_num >= 1 and consonant_num >= 2:
            print("".join(code)) # 암호 출력
        return

    # start 지점부터 탐색
    for i in range(start, c):

        # 중복 허용하지 않으므로 암호에 있는 문자이면 pass
        if letters[i] in code:
            continue

        code.append(letters[i]) # 현재 문자를 암호에 추가
        backtracking(i+1) # 알파벳 순서가 큰 문자만 암호에 추가될 가능성 있음
        code.pop()

# 첫 번째 문자부터 백트래킹 수행
backtracking(0)