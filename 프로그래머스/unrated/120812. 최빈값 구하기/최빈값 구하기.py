import collections
def solution(array):

    if len(array) == 1:
        return array[0]

    counter = collections.Counter(array)

    first = counter.most_common()[0]
    second = counter.most_common()[1]

    if first[1] == second[1]:
        return -1
    else:
        return first[0]