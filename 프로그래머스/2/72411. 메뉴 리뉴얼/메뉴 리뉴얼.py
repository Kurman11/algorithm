from itertools import combinations

def solution(orders, course):
    answer = []
    length_filter = {}
    for order in orders:
        for i in range(2, len(order) + 1):
            for j in combinations(order, i):
                word = ''.join(sorted(list(j)))
                if word in length_filter:
                    length_filter[word] += 1
                else:
                    length_filter[word] = 1

    length_list = sorted(length_filter.items(), key=lambda x:x[1], reverse=True)
    length_dict = {}

    for tupl in length_list:
        if tupl[1] < 2:
            continue
        length = len(tupl[0])
        if length not in course:
            continue
        if length in length_dict:
            if length_dict[length] == tupl[1]:
                answer.append(tupl[0])
        else:
            length_dict[length] = tupl[1]
            answer.append(tupl[0])

    answer.sort()
    return answer