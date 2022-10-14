def solution(board, moves):
    answer = 0
    bucket = []

    for i in range(len(moves)):
        for j in range(0, len(board)):
            if board[j][moves[i]-1] != 0:
                if len(bucket) > 0 and bucket[-1] != board[j][moves[i]-1]:
                    bucket.append(board[j][moves[i]-1])
                elif len(bucket) > 0 and bucket[-1] == board[j][moves[i]-1]:
                    bucket.pop()
                    answer += 1
                elif len(bucket) == 0:
                    bucket.append(board[j][moves[i]-1])
                board[j][moves[i]-1] = 0
                break
        
    return answer * 2