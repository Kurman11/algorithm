import math

def solution(brown, yellow):
    answer = []
    
    S=brown+yellow #카펫 너비
    b=(brown+4)/2
    w, h = 0, 0 #카펫의 가로 길이와 세로 길이
    answer.append(int((b+math.sqrt(b**2-4*S))/2))
    answer.append(int((b-math.sqrt(b**2-4*S))/2))
    return answer