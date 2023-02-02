num = int(input())
num1 = list(map(int,input().split()))
cnt = 0
a = []
for i in range(1,num):
    if num1[i] > num1[i-1]:
        cnt += num1[i] - num1[i-1]
        a.append(cnt)
        if num1[i] == num1[i-1]:
            a.append(cnt)
    else:
        a.append(cnt)
        cnt = 0
print(max(a))