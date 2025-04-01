def solution(s):
    left = 0
    right = 0
    for i in s:
        if i == '(':
            left += 1
        elif i == ')':
            if left == 0:
                right += 1
            else:
                left -= 1
    
    if left == 0 and right == 0 :    
        answer = True
    else:
        answer = False
    
    return answer