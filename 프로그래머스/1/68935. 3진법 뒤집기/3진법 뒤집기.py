def solution(n):
    s = []
    while n != 0:
        s.append(n % 3)
        n //= 3
    
    return int(''.join(map(str, s)), base=3)