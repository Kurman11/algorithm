T = int(input())

num = list(map(int,input().split()))
cnt = 0
a = 0
b = []
for i in sorted(num):
    if a != i:
        b.append(cnt)
        a = i
        cnt += 1
    else:
        b.append(cnt-1)

d = dict(zip(sorted(num),b))

for i in num:
    print(d.get(i), end=' ')