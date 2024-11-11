T = int(input())

for i in range(1, T+1):
    N = int(input())
    b = N
    a = set()
    cnt = 0
    while 1:
        cnt += 1
        for j in str(N):
            a.add(int(j))
        
        if len(a) == 10:
            break
        else:
            N = N + b

    print(f'#{i} {N}')