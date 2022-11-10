def solution(ingredient):
    answer = 0    
    stack = []
    
    for i in range(len(ingredient)):
        # 스택에 재료 넣기
        stack.append(ingredient[i])
            
        n = len(stack)

        if n >= 4:
            # 빵, 야채, 고기, 빵
            if stack[n-4]==1 and stack[n-3]==2 and stack[n-2]==3 and stack[n-1]==1:
                # 4개 재료 스택에서 제거
                for _ in range(4):
                    stack.pop()
                
                # 버거 개수 +1 
                answer += 1

    return answer