a = []
d = dict()

for i in range(10):
    num = input()
    a.append(int(num))
print(sum(a)//10)


for x in a:
    if x not in d:
        d[x] = 1
    else:
        d[x] = d[x] +1

for key,value in d.items():
    if max(d.values()) == value:
        print(key)
