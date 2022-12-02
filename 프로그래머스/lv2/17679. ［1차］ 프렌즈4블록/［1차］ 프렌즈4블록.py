def solution(m, n, board):

    for i in range(m):
        board[i] = list(board[i])

    # 지워진 블록 개수
    answer = 0
    
    # 지워질 블록의 좌표 저장할 집합
    removed = set()

    while True:
        for i in range(m-1):
            for j in range(n-1):
                # 현재 블록
                cur = board[i][j]

                # 이미 지워진 블록은 제외
                if not cur:
                    continue
                
                # 2x2 블록이 모두 같은 블록인지 확인
                if board[i][j+1] == cur and board[i+1][j] == cur and board[i+1][j+1] == cur:
                    # 2x2 블록 좌표를 집합에 추가
                    removed.add((i,j))
                    removed.add((i,j+1))
                    removed.add((i+1,j))
                    removed.add((i+1,j+1))
        
        # 삭제된 블록이 있는 경우
        if removed:
            # 삭제한 블록 개수 = 집합 길이
            answer += len(removed)

            # 삭제 표시를 위해 해당 좌표 값을 지움
            for i, j in removed:
                board[i][j] = []
            
            # 삭제한 블록 좌표 정보 초기화
            removed = set()
        
        # 삭제된 블록 없으면 종료
        else:
            return answer

        # 블록 위에서 아래로 당기기
        while True:
            moved = False

            # 당길 값이 없을 때까지 반복해서 한 줄씩 이동
            for i in range(m-1):
                for j in range(n):
                    # 현재 줄엔 블록이 있고, 아래 줄엔 블록이 없는 경우
                    if board[i][j] and not board[i+1][j]:
                        # 윗 줄의 블록을 아래로 이동
                        board[i+1][j] = board[i][j]
                        # 현재 줄의 블록은 비었다고 표시
                        board[i][j] = []
                        # 이동시킨 블록이 있음을 표시
                        moved = True
                        
            # 더 이상 당길 블록이 없으면 종료
            if not moved:
                break