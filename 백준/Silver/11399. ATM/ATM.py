T =int(input())
num = list(map(int,input().split()))
a = []
cnt = 0
num = sorted(num)
while 1:
    a.append(num.pop(0))
    cnt += sum(a)

    if len(num) == 0:
        break

print(cnt)