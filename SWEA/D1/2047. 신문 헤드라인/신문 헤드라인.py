T = list(map(str,input()))
a = []

for i in T:
    if i.isupper() == True:
        a.append(i)
    else:
        a.append(i.upper())

rst =''.join(a)
print(rst)