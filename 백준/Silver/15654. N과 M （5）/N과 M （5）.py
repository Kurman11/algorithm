def dfs(n,rst):
    if M == n:
        ans.append(rst)
        return
    for i in range(N):
        if v[i] == 0:
            v[i] = 1
            dfs(n+1 , rst+[lst[i]])
            v[i] = 0

N, M = map(int,input().split())
lst = sorted(list(map(int,input().split())))
v = [0] * N
ans = []

dfs(0,[])

for i in ans:
    print(*i)