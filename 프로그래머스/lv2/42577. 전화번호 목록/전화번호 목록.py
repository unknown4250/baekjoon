def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        prefix = phone_book[i]
        compared = phone_book[i+1]

        # 해당 번호가 다음 번호의 접두사인 경우
        if prefix in compared and compared.index(prefix) == 0:
            return False
    return True
