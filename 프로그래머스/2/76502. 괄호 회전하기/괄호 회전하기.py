def solution(s) :
    answer = 0
    temp = [i for i in s]

    for i in range(len(temp)) :
        temp.append(temp.pop(0))
        left = []
        cnt = len(temp)

        for j in temp :
            cnt -= 1
            if j == "[" or j == "(" or j == "{" : # 여는 괄호를 left에 삽입
                left.append(j)
            elif j == "}" : # 닫는 괄호일 경우 left에서 꺼내 확인
                if len(left) == 0 or left.pop() != "{" :
                    cnt = 10
                    break
            elif j == "]" :
                if len(left) == 0 or left.pop() != "[" :
                    cnt = 10
                    break
            elif j == ")" :
                if len(left) == 0 or left.pop() != "(" :
                    cnt = 10
                    break

        if cnt == 0 and len(left) == 0 :
            answer += 1

    return answer