str1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
str2 = input()

for i in str1:
    if i in str2:
        print(str2.index(i), end=' ')
    elif i not in str2:
        print(-1, end=' ')