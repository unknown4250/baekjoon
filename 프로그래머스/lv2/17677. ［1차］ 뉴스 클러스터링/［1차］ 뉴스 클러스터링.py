from math import floor

def solution(str1, str2):

    arr1, arr2 = [], []

    # str1의 다중 집합
    for i in range(len(str1)-1):
        # 이어진 두 글자가 영문자인 경우만 저장
        if str1[i].isalpha() and str1[i+1].isalpha():
            arr1.append(str1[i:i+2].lower())
    
    # str2의 다중 집합
    for i in range(len(str2)-1):
        # 이어진 두 글자가 영문자인 경우만 저장
        if str2[i].isalpha() and str2[i+1].isalpha():
            arr2.append(str2[i:i+2].lower())

    # &(and), |(or) 연산으로 교집합, 합집합 구하기
    intersection = set(arr1) & set(arr2)
    union = set(arr1) | set(arr2)

    # 두 집합이 공집합인 경우
    if len(union) == 0:
        return 65536

    # 교집합 길이
    intersection_len = sum([min(arr1.count(i), arr2.count(i)) for i in intersection])

    # 합집합 길이
    union_len = sum([max(arr1.count(u), arr2.count(u)) for u in union])

    return floor((intersection_len / union_len) * 65536)