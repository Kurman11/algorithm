def solution(n):
    answer = 0
    a = bin(n)
    b = a.count('1')
    while 1:
        n += 1
        c = bin(n)
        d = c.count('1')
        if b == d:
            return n
    return answer