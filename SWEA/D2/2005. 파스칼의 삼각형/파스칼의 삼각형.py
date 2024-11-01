N = int(input())
for tc in range(1, N+1):
    T = int(input())
    a = [[0]*T for _ in range(T)]
    a[0][0] = 1
    for i in range(1, T):
        for j in range(T):
            if j == 0:
                a[i][j] = 1
            else:
                a[i][j] = a[i-1][j-1] + a[i-1][j]
        
    print('#{}'.format(tc))
    for k in range(T):
        for l in range(T):
            if a[k][l]:
                print(a[k][l], end=' ')
        print()