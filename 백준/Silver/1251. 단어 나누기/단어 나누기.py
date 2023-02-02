list1=[]
num = input()
for i in range(1, len(num)):
    for x in range(i+1,len(num)):
        a = num[:i][::-1]
        b = num[i:x][::-1]
        c = num[x:][::-1]
        list1.append(a+b+c)
list1.sort()
print(list1[0])