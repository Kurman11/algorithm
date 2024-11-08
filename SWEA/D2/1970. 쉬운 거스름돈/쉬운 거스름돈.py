T = int(input())
a = [50000,10000,5000,1000,500,100,50,10]

for i in range(1, T+1):
    N =int(input())
    b = []

    for j in a:
        if N >= j:
            c = N // j
            N = N % j
            b.append(c)
        else:
            b.append(0)
    print(f'#{i}')
    print(*b)