def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]


    for str in babbling:
        # 발음할 수 있는 단어
        for word in words:
            # 같은 문자를 반복해서 포함하면 안됨
            if word * 2 not in str:
                # 발음할 수 있는 단어 포함되어 있으면 공백으로 변경
                str = str.replace(word, " ")

        # 공백이면 모든 단어를 발음할 수 있으므로 +1
        if str.strip() == "":
            answer += 1

    return answer