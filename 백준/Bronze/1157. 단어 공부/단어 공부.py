word = input().upper()
a =[]
b =[]
c =[]
cnt = 0
for i in word:
    a.append(i)


for x in set(a):
    b.append(a.count(x))
    

for t in set(a):
    if max(b) == a.count(t):
        c.append(t)

if len(c) != 1:
    print('?')
else:
    print(*c)