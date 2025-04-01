def solution(s):
    word = s.split(' ')
    for i in range(len(word)):
        if word[i]:
            word[i] = word[i][0].upper() + word[i][1:].lower()
    
    answer = ' '.join(word)
    return answer