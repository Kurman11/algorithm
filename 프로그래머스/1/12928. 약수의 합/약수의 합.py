def solution(n):
    data = []
    for i in range(n//2, 0, -1) :
        if n % i == 0 :
            data.append(i)
    data.append(n)
    
    result = sum(data)
    return result