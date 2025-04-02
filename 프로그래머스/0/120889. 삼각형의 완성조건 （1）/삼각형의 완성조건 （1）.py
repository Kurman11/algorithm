def solution(sides):
    sides.sort()
    if sides[-1] < sides[0] + sides[1]:
        answer = 1
    else:
        answer = 2
    return answer