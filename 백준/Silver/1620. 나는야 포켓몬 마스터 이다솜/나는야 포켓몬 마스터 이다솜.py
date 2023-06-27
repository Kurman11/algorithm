num = list(map(int,input().split()))

a = []
for i in range(num[0]):
    a.append(input())

c = {}

for i, s in enumerate(a):
    c[s] = str(i+1)

for i in range(num[1]):
    q = input()
    if q.isdecimal() == True:
        print(a[int(q)-1])
    else:
        print(c[q])