def solution(s):
    # 문자열의 첫 번째 문자를 스택에 미리 넣어두기
    stack = [s[0]]

    for i in range(1, len(s)):
        # 스택에 값이 있으면서 직전 문자와 같은 문자면 스택에서 제거
        if stack and stack[-1] == s[i]:
            stack.pop()
        # 스택이 비었거나 직전 문자와 다른 문자면 스택에 추가
        else:
            stack.append(s[i])
    
    # 스택이 비었으면 문자열 모두 제거했으므로 1 리턴, 아니라면 0 리턴
    return 1 if not stack else 0
