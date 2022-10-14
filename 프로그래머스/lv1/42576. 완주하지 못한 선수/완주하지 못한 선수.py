from collections import Counter

def solution(participant, completion):
    not_completed = Counter(participant) - Counter(completion)
    answer = list(not_completed.keys())[0]
    return answer