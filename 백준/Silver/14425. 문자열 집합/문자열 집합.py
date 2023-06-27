num = list(map(int,input().split()))
a = []
b = []
cnt = 0
for i in range(num[0]):
    a.append(input())

a = set(a)

for i in range(num[1]):
    b.append(input())

for i in b:
    if i in a:
        cnt += 1

print(cnt)