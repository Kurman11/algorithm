def solution(n):
    cnt = 0
    while 1:
        cnt += 1
        if n % cnt == 1:
            break
    answer = cnt
    return answer