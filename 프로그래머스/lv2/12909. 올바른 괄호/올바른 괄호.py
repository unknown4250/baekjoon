def solution(s):
    
    stack = []

    for ch in s:
        if ch == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
        else:
            stack.append(ch)

    return True if not stack else False
