a = []
b = []
c = []
for i in range(3):
    num = int(input())
    a.append(num)

if sum(a) == 180:
    while len(a) > 0 :
        if a[0] == 60:
            b.append(a.pop(0))            
        else:
            c.append(a.pop(0))


    if len(c) == 3:
        if c[0] == c[1]:
            print('Isosceles')
        elif c[1] == c[2]:
            print('Isosceles')
        elif c[0] == c[2]:
            print('Isosceles')
        else:
            print('Scalene')
    elif len(c) == 2:
        if c[0] == c[1]:
            print('Isosceles')
        else:
            print('Scalene')
    elif len(c) == 0:
        print('Equilateral')
else:
    print('Error')