from itertools import combinations

def solution(numbers) :
    answer = []
    for value in combinations(numbers, 2) :
        answer.append(sum(value))

    answer = list(set(answer))
    answer.sort()
    return answer