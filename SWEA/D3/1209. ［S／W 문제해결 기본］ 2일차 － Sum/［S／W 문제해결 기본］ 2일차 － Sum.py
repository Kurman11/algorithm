for i in range(1, 11):
    T = int(input())
    N = 100
    arr = [list(map(int,input().split())) for _ in range(N)]
    rst = []
    for j in range(N):
        a = 0
        b = 0
        c = 0
        d = 0
        for k in range(N):
            a += arr[j][k]
            b += arr[k][j]
            c += arr[k][k]
        rst.append(a)
        rst.append(b)
        rst.append(c)

        for k in range(N-1,-1,-1):
            d += arr[k][k]
        rst.append(d)

    print(f'#{i} {max(rst)}')