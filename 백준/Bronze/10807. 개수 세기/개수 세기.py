T = int(input())

num = list(map(int,input().split()))
num1 = int(input())
cnt = 0
for i in num:
    if num1 == i:
        cnt += 1

print(cnt)