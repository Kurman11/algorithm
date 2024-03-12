def solution(phone_book) :
    phone_book.sort()
    for i in range(len(phone_book) - 1) :
        index = len(phone_book[i])
        if phone_book[i] in phone_book[i+1][:index] :
            return False

    return True