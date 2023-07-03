def parse(str):
    correct = True
    left = 0
    right = 0
    mystack = []
    
    for i in range(len(str)):
        if str[i] == '(':
            left += 1
            mystack.append('(')
        else:
            right += 1
            if len(mystack) == 0:
                correct = False
            else:
                mystack.pop()
                
        if left == right:
            return i + 1, correct
    return 0, False

def solution(p):
    if len(p) == 0:
        return p
    
    pos, correct = parse(p)
    u = p[:pos]
    v = p[pos:]
    
    if correct:
        return u + solution(v)
    
    answer = '(' + solution(v) + ')'
    for i in range(1, len(u)-1):
        if u[i] == '(':
            answer += ')'
        else:
            answer += '('
        
    return answer