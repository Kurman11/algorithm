def simple(x):
    d = 2
    while d <= x:
        if x % d == 0:
            a.append(d)
            x = x / d
        else:
            d = d + 1


num = int(input())

for i in range(1,num+1):
    a = []
    simple(int(input()))
    print(f'#{i} {a.count(2)} {a.count(3)} {a.count(5)} {a.count(7)} {a.count(11)}')