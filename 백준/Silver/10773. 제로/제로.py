T = int(input())
a = []
for t in range(1, T+1):
    num = list(map(int,input().split()))
    for i in num:
        if i == 0:
            a.pop()
        else:
            a.append(i)
print(sum(a))