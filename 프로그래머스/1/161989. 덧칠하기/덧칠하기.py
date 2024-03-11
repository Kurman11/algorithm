def solution(n, m, section):
    answer = 0
    start = -100001
    
    for s in section:
        if s>=start+m:
            start = s
            answer += 1
    return answer