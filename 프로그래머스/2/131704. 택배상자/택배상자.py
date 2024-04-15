from collections import deque

def solution(order):
    N = len(order)
    tmp = [0]*N
    for idx, odr in enumerate(order) :
        tmp[odr-1] = idx+1
    rev_order = deque(list())
    answer = 1
    for odr in tmp :
        if odr != answer :
            rev_order.append(odr)
            continue
        answer += 1
        while rev_order and answer == rev_order[-1] :
            rev_order.pop()
            answer += 1
            
    return answer - 1