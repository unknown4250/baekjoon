def solution(prices):
    answer = [0] * len(prices)

    # 현재 주식 가격 시점
    for i in range(len(prices)-1):
        # 현재 이후의 주식 가격 시점
        for j in range(i+1, len(prices)):
            # 1초 증가
            answer[i] += 1

            # 가격이 떨어진 경우
            if prices[i] > prices[j]:
                break

    return answer
