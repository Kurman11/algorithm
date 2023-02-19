a = []
b = []
c = {}
for i in range(28):
    num = int(input())
    a.append(num)

for x in range(1,31):
    b.append(x)

c = set(b) - set(a)
print(min(c))
print(max(c))