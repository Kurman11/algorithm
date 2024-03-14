from collections import deque

def solution(numbers, target):
    answer = 0
    
    q = deque()
    q.append((numbers[0], 0))
    q.append((-numbers[0], 0))
    
    while q:
        n, order = q.popleft()
        
        if order == len(numbers)-1:
            if n == target:
                answer += 1
            continue
        
        q.append((n+numbers[order+1], order+1))
        q.append((n-numbers[order+1], order+1))
    
    return answer