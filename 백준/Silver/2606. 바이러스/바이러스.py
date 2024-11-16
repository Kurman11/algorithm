def dfs(c):
    ans_dfs.append(c)
    v[c] = 1

    for i in arr[c]:
        if not v[i]:
            dfs(i)

T = int(input())
n = int(input())
arr = [[] for _ in range(T+1)]


for i in range(n):
    s, e = map(int,input().split())
    arr[s].append(e)
    arr[e].append(s)

ans_dfs = []
v = [0] * (T+1)
dfs(1)
print(len(ans_dfs)-1)