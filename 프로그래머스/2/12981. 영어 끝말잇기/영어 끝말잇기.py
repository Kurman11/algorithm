def solution(n, words):
    num = len(words)
    answer = []
    cnt = 1
    word = [words[0]]
    words.pop(0)
    for i in words:
        if i in word or word[-1][-1] != i[0]:
            break
        else:
            cnt += 1
            word.append(i)
    
    a, b = divmod(cnt, n)
    
    if num == cnt:
        return [0,0]
            
    return [b+1 , a+1]