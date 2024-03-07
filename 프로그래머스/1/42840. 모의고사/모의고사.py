def solution(answers):
    answer = []
    length = len(answers)
    temp2 = [2, 1, 2, 3, 2, 4, 2, 5]
    temp3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a = []
    b = []
    c = []

    for i in range(length):
        a.append(i % 5 + 1)

    for i in range(length):
        if (i % 2) == 0:
            b.append(temp2[i % 8])
        else:
            b.append(temp2[i % 8])

    for i in range(length):
        if (i % 10) < 2:
            c.append(temp3[0])
        elif (i % 10) < 4:
            c.append(temp3[2])
        elif (i % 10) < 6:
            c.append(temp3[4])
        elif (i % 10) < 8:
            c.append(temp3[6])
        else:
            c.append(temp3[8])

    a_count = 0
    b_count = 0
    c_count = 0
    for i in range(len(answers)):
        if answers[i] == a[i]:
            a_count += 1
        if answers[i] == b[i]:
            b_count += 1
        if answers[i] == c[i]:
            c_count += 1

    if max(a_count, b_count, c_count) == a_count:
        answer.append(1)
    if max(a_count, b_count, c_count) == b_count:
        answer.append(2)
    if max(a_count, b_count, c_count) == c_count:
        answer.append(3)

    answer.sort()
    return answer