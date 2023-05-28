num = input()
a = []
b = []
c = []
for i in num:
    a.append(i)

for i in a:
    b.append(int(i))

for i in sorted(b)[::-1]:
    print(i,end='')