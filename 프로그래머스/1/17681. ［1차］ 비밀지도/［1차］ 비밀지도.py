
def solution(n, arr1, arr2) :
    answer = []
    temp1 = []
    temp2 = []
    for value in arr1 :
        value = bin(value)[2:]
        value = '0' * (n - len(value)) + value
        temp1.append(value)

    for value in arr2 :
        value = bin(value)[2:]
        value = '0' * (n - len(value)) + value
        temp2.append(value)

    for i in range(n) :
        value = ""
        for j in range(n) :
            if temp1[i][j] == '0' and temp2[i][j] == '0' :
                value += " "
            else :
                value += "#"
        answer.append(value)

    return answer