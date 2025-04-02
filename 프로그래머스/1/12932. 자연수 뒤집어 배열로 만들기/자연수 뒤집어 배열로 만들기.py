def solution(n):
    answer = []
    n = str(n)
    n = ''.join(reversed(n))
    for i in n:
        answer.append(int(i))
    
    return answer