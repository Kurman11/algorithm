from collections import Counter

def solution(want, number, discount):
    answer = 0
    targetcnt = Counter({item:cnt for item, cnt in zip(want, number)})

    # 처음 열흘을 우선 판단해봅니다.
    currcnt = Counter(discount[:10])
    if targetcnt == currcnt:
        answer += 1
    # 하루씩 늘려가면서, i일째의 항목을 1개 추가하되 i-10일째의 항목을 1개 빼고 판단합니다.
    for i in range(10, len(discount)):
        currcnt[discount[i]] += 1
        currcnt[discount[i-10]] -= 1
        # 주의) 뺀 항목이 0개가 되면 그 항목을 카운터에서 제거해주어야 합니다.
        if currcnt[discount[i-10]] == 0:
            currcnt.pop(discount[i-10])

        if targetcnt == currcnt:
            answer += 1
            
    return answer