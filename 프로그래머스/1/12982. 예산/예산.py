def solution(d, budget) :
    d.sort()
    temp_sum = 0
    answer = 0
    for i in range(len(d)) :
        if temp_sum + d[i] > budget :
            break
        temp_sum += d[i]
        answer += 1

    return answer