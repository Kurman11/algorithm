A = int(input())
B = int(input())
C = int(input())

product = A * B * C


d = dict()
for i in str(product):
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i] +1
for x in range(10):
    if str(x) not in d.keys():
        d[str(x)] = 0

for key,velue in sorted(d.items()):
    print(velue)