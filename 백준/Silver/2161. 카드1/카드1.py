num = int(input())

a = list(range(1, num+1))
b = []
while len(a) > 1:
    b.append(a.pop(0))
    a.append(a.pop(0))
print(*b , *a)