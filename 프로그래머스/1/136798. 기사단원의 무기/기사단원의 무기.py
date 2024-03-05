def nd(n):
    ret = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i**2 != n:
            	ret += 2
            else:
                ret += 1
    return ret
        
def solution(number, limit, power):
    print(nd(2))
    answer = 0
    for n in range(1, number+1):
        s = nd(n)
        if s > limit:
            answer += power
        else:
            answer += s
            
    return answer