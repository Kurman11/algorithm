def solution(msg):
    d = {a:i for i, a in enumerate('abcdefghijklmnopqrstuvwxyz'.upper(), 1)}
    idx = 27
    
    i = 0
    answer = []
    while i < len(msg):
        # 지금 위치에서 확인해볼 문자열의 길이 
        l = 1
        
        # 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
        while msg[i:i+l+1] in d and i+l+1 <= len(msg):
            l += 1
        w = msg[i:i+l]

        # w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
        answer.append(d[w])
        # 입력에서 처리되지 않은 다음 글자가 남아있다면,
        # w+c에 해당하는 단어를 사전에 등록한다.
        if i+l+1 <= len(msg):
            d[msg[i:i+l+1]] = idx
            idx += 1
        i += l
        
    return answer