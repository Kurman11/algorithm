def solution(s) :
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key=len)

    for i in s :
        data = i.split(",")
        for value in data :
            if int(value) not in answer :
                answer.append(int(value))

    return answer