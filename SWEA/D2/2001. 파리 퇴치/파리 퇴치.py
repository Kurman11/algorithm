def dfs(a,b):
    z = 0
    v[a][b] = 1
    for q in range(e):
        for w in range(e):
            z += arr[a + q][b + w]

    rst.append(z)
    for i in range(0, (s-e)+1):
        for j in range(0, (s-e)+1):
            if not v[i][j]:
                dfs(i,j)


T = int(input())
for i in range(1, T+1):
    s, e = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(s)]
    v = [[0 for _ in range(s)] for _ in range(s)]
    rst= []
    dfs(0,0)
    print(f'#{i} {max(rst)}')