def solution(s):
    
    answer = 0

    pair = {"]": "[", ")": "(", "}": "{"}

    for i in range(len(s)):
        # 문자열을 한 칸씩 회전
        string = s[i:] + s[:i]

        # 스택
        stack = []
        
        # 올바른 괄호 문자인지 확인하기 위한 플래그
        flag = True

        for ch in string:
            # 여는 괄호인 경우, 스택에 삽입
            if ch not in pair:
                stack.append(ch)
            # 닫는 괄호인 경우
            else:
                # 스택이 비어있거나 스택의 마지막 문자열과 짝이 되지 않는 경우
                if not stack or pair[ch] != stack[-1]:
                    # 플래그를 false로 설정
                    flag = False
                    # 해당 문자열의 탐색 종료
                    break
                # 짝이 되는 괄호이므로 스택에서 제거
                else:
                    stack.pop()
        
        # 플래그가 true이면서 스택이 비었다면 올바른 괄호인 경우
        if flag and not stack:
            answer += 1

    return answer