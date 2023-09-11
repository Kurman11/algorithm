word = input()
word_1 = input()
a = [0] * len(word_1)

for i in range(len(word)):
    cnt = 0
    for j in range(len(word_1)):
        if cnt < a[j] :
            cnt = a[j]
        elif word[i] == word_1[j]:
            a[j] = cnt + 1

print(max(a))