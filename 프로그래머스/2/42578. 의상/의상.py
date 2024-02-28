def solution(clothes) :
    answer = 1
    info = {}
    for cloth in clothes :
        cloth_type = cloth[1]
        if cloth_type in info :
            info[cloth_type] += 1
        else :
            info[cloth_type] = 2

    for value in info.values() :
        answer *= value

    return answer - 1