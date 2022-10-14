def solution(board, moves):
    answer = 0
    bucket = []

    for i in range(len(moves)):
        for j in range(0, len(board)):
            # 크레인이 멈춘 위치에 인형이 있는 경우
            if board[j][moves[i]-1] != 0:
                # 바구니에 인형이 없거나, 마지막 인형과 같지 않은 경우
                if len(bucket) == 0  or (len(bucket) > 0 and bucket[-1] != board[j][moves[i]-1]):
                    bucket.append(board[j][moves[i]-1])
                # 마지막 인형과 같은 인형이 연속해서 쌓인 경우
                elif len(bucket) > 0 and bucket[-1] == board[j][moves[i]-1]:
                    bucket.pop()
                    answer += 1
                # 같은 위치를 다시 방문하지 않기 위해 0으로 변경
                board[j][moves[i]-1] = 0
                break
                
    # 제거된 인형 개수 = 인형 제거 횟수 * 2
    return answer * 2
