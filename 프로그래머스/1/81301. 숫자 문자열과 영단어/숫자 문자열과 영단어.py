def solution(s):
    num_a = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    ans = ''
    alp = ''
    for i in range(len(s)):
        if s[i].isdigit(): # 숫자이면
            ans += s[i] # 그대로 출력
        else: # 숫자가 아니면
            alp += s[i]
            if alp in num_a:
                ans += str(num_a.index(alp))
                alp = ''
            else:
                continue
        
    answer = int(ans)
    return answer