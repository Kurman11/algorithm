def solution(s):
    answer = 0
    cnt = [0, 0]  # [x의 개수, x가 아닌 글자들의 갯수]
    cur = 0
    while True:
        flag = False
        for i in range(cur, len(s)):
            if cnt[0] == cnt[1] and cnt[0] != 0:
                answer+=1
                cnt = [0,0]
                cur = i
                break
            if s[cur] != s[i]:
                cnt[1] += 1
            else:
                cnt[0] += 1
            if i == len(s)-1:
                flag = True
        if flag:
            break
    return answer+1