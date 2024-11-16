for i in range(1,11):
    M, N = map(str,input().split())

    cnt = 0

    while cnt < len(N)-1:
        if int(N[cnt]) == int(N[cnt+1]):
            N = N[:cnt] + N[cnt + 2:]
            cnt = max(0, cnt-1)
        else:
            cnt += 1

    print(f'#{i} {N}')