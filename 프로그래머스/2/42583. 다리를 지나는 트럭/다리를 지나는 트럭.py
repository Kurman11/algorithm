from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    q = deque(truck_weights)
    onboard = deque([0 for _ in range(bridge_length)])
    
    onweight = q.popleft()
    onboard.append(onweight)
    onboard.popleft()
    
    while onweight:
        if onboard.popleft():
            onweight = sum(onboard)
        if q:
            if onweight + q[0] <= weight:
                onboard.append(q.popleft())
                onweight = sum(onboard)
            else:
                onboard.append(0)
        answer += 1

    return answer