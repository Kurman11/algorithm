def solution(n, s):
    
    if n > s:
        return [-1]
    
    div = s // n
    remain = s % n
    
    answer = [div] * n
    
    for i in range(remain):
        answer[i] = answer[i] + 1
    
    answer.sort()
    return answer