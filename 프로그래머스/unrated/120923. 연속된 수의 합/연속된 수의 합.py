def solution(num, total):
    answer = []    
    answer += [num + 1 for num in range(num)]
    
    move = (total - sum(answer)) // num

    for i in range(len(answer)):
        answer[i] += move

    return answer
