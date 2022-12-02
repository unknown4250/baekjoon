def solution(files):
    answer = []
    
    # 파일명을 HEAD, NUMBER, TAIL로 파싱
    for file in files:
        head, number, tail = "", "", ""

        for i in range(len(file)):
            # 파일명 중 첫 번째 숫자인 경우
            if file[i].isdigit():
                # HEAD, NUMBER 구분
                head = file[:i]
                
                tail_idx = i

                # NUMBER, TAIL 구분
                while tail_idx < len(file):
                    if file[tail_idx].isdigit(): 
                        tail_idx += 1
                    else:
                        break
                
                number = file[i:tail_idx]
                tail = file[tail_idx:]
                
                answer.append([head, number, tail])
                break
            
    # HEAD, NUMBER 기준으로 정렬
    answer = sorted(answer, key=lambda x:(x[0].lower(), int(x[1])))

    return ["".join(i) for i in answer]