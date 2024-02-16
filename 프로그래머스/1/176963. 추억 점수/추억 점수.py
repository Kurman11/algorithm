def solution(name, yearning, photo):
    result = []
    
    score_dict = {}
    for a,b in zip(name,yearning): # 이름:스코어 딕셔너리
        score_dict[a] = b
    
    for case in photo:
        tmp = 0 # 케이스별로 점수 초기화
        for idx in range(len(case)):
            if case[idx] not in score_dict: # 이름 없으면 패스
                continue
            else: # 이름 있으면 점수 상승
                tmp += score_dict[case[idx]]
        result.append(tmp)
    
    return result