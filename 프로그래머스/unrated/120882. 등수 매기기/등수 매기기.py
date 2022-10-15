import collections
def solution(score):
    answer = [0] * len(score)

    dict = collections.defaultdict(list)

    for i in range(len(score)-1, -1, -1):
        if sum(score[i]) in dict:
            dict[sum(score[i])].append(i)
        else:
            dict[sum(score[i])] = [i]
    dict = sorted(dict.items(), reverse=True)
    
    rank = 1
    for k, v in dict:
        cnt = 0
        while len(v) > 0:
            answer[v.pop()] = rank
            cnt += 1
        rank += cnt
    
    return answer
