T = int(input())


for i in range(1, T+1):
    N = int(input())
    a = []
    for j in range(1, N+1):
        if j % 2 == 1:
            a.append(j)
        else:
            a.append(-j)

    print(f'#{i} {sum(a)}')