def solution(n):
    pz = 7
    if n <= pz:
        answer = 1
    elif n > pz :
        if n % pz == 0:
            answer = (n//pz)
        else:
            answer = (n // pz) + 1 
    return answer