num1 = int(input())
num_1 = list(map(int,input().split()))

num2 = int(input())
num_2 = list(map(int,input().split()))

cnt ={}

for i in num_1:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in num_2:
    if i in cnt:
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')