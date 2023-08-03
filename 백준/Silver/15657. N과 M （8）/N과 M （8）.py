def dfs(n,rst,last_num):
    if M == n:
        ans.append(rst)
        return
    for i in range(N):
        if v[i] >= 0 and i >= last_num:
            v[i] = 1
            dfs(n+1 , rst+[lst[i]],i)
            v[i] = 0

N, M = map(int,input().split())
lst = sorted(list(map(int,input().split())))
v = [0] * N
v_1 = [0] * N

ans = []

dfs(0,[],-1)

for i in ans:
    print(*i)