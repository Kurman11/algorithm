def solution(s):
    a = []
    
    for i in s:
        if not a:
            a.append(i)
        else:
            if a[-1] == i:
                a.pop()
            else:
                a.append(i)
    
    if a :
        return 0
    
    
    return 1