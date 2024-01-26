def solution(s):
    answer = []
    split_s = s.split(' ') # 문자열을 공백을 기준으로 분리
    for s in split_s:
        tmp = ''
        for idx, w in enumerate(s):
            if idx % 2 == 0: # 짝수인 경우
                tmp += w.upper()
            else: # 홀수인 경우
                tmp += w.lower()
        answer.append(tmp) 
    return ' '.join(answer)