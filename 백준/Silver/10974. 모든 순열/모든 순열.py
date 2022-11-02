import sys
input = sys.stdin.readline

n = int(input())
answer = []


def backtracking():
    # 수열 길이가 M이라면 출력
    if len(answer) == n:
        print(*answer)
        return
    
    # 사전 순으로 증가하며 수열 생성
    for i in range(1, n+1):

        # 수열에 없다면 추가
        if i not in answer:
            answer.append(i) # 정답 배열에 추가
            backtracking()
            answer.pop() # 중복 없이 수열을 만들기 위해 배열에 넣었던 값은 다시 뺌

backtracking()