def solution(n):
    answer = n ** (1/2)
    if answer % 1 == 0:
        result = 1
    else:
        result = 2
    return result