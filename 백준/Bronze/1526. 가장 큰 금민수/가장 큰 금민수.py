num = int(input())
a = []
for i in range(4,num+1):
    cnt = 0 
    for x in range(len(str(i))):
        if str(i)[x] == '4' or str(i)[x] =='7':
            cnt +=1
        else:
            break

        if cnt == len(str(i)):
            a.append(i)
print(max(a))