def solution(s):
    a = []
    
    for i in s:
        if i == '(':
            a.append(i)
        else:
            if len(a) == 0:
                return False
            else:
                a.pop()
    if len(a) != 0:
        return False

    return True