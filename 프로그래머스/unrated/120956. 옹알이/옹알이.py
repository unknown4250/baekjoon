def solution(babbling):
    posibilities = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for b in babbling:
        for p in posibilities:
            if p * 2 not in b:
                b = b.replace(p, ' ')
        if len(b.strip()) == 0:
            answer += 1
    return answer