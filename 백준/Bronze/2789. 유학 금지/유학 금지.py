str1 = list(input())
str2 = list('CAMBRIDGE')
a = []
for i in str1:
    if i not in str2:
        a.append(i)   

for x in a:
    print(x,end='')