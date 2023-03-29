T = int(input())
num = list(map(int,input().split()))
cnt = 0
for i in num:
    error = 0
    if i > 1:
        for x in range(2,i):
            if i%x==0:
                error += 1       
        if error == 0:
            cnt +=1

print(cnt)