for i in range(1,11):
    T = int(input())
    word = input()
    word_str = input()
    N= len(word)
    cnt = 0

    for j in range(len(word_str)):
        if word_str[j:j+N] == word:
            cnt += 1
        
    print(f'#{i} {cnt}')