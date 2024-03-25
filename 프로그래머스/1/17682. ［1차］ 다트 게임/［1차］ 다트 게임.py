def solution(dartResult):
    # 0. 입력 및 초기화
    scores = []
    start_idx = 0
    power = {'S' : 1, 'D' : 2, 'T' : 3 }

    # 1. dartResult 별로 처리
    for i in range(len(dartResult)):
        op = dartResult[i]
        if op in power:
            scores.append(int(dartResult[start_idx:i]) ** power[op])
        elif op == '*':
            scores[-2:] = [x * 2 for x in scores[-2:]]
        elif op == '#':
            scores[-1] = -scores[-1]

        if not op.isnumeric():
            start_idx = i + 1

    # 2. scores의 합을 반환
    return sum(scores)


solution('1S2D*3T')
