def solution(numbers, hand):
    answer = ''
    
    # 왼손 *, 오른손 # 시작
    left = 10
    right = 12
    
    for n in numbers:
        # 계산을 위해 0을 11로 치환
        if n == 0:
            n = 11
            
        # 1, 4, 7 -> 왼손
        if n % 3 == 1:
            answer += 'L'
            left = n
            
        # 3, 6, 9 -> 오른손
        elif n % 3 == 0:
            answer += 'R'
            right = n
        
        # 2, 5, 8, 11(0)
        else:
            # 현재 키패드와 왼손, 오른손과의 거리 측정
            mL = abs(n - left)
            mR = abs(n - right)
            
            # 이동할 거리 계산
            dL = (mL // 3) + (mL % 3)
            dR = (mR // 3) + (mR % 3)
            
            # 왼손이 더 가까운 경우
            if dL > dR:
                answer += 'R'
                right = n
            
            # 오른손이 더 가까운 경우
            elif dL < dR:
                answer += 'L'
                left = n
            
            # 이동 거리가 같다면 왼손잡이/오른손잡이에 따라 다름
            else:
                if hand == 'left':
                    answer += 'L'
                    left = n
                else:
                    answer += 'R'
                    right = n
    return answer