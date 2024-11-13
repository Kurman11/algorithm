def dfs(n):
    global ans,v
    if n == P:
        ans = max(ans, int("".join(map(str,arr))))
        return
    
    for i in range(L-1):
        for j in range(i+1, L):
            arr[i], arr[j] = arr[j], arr[i]
            
            chk = int("".join(map(str,arr)))
            if (n,chk) not in v:
                dfs(n+1)
                v.append((n,chk))
            arr[i], arr[j] = arr[j], arr[i]
    



T = int(input())

for i in range(1,T+1):
    N, P = map(str,input().split())
    P = int(P)
    arr = []
    for j in N:
        arr.append(int(j))
    
    L = len(arr)
    ans = 0
    v = []

    dfs(0)
    print(f'#{i} {ans}')