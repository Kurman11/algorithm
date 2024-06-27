def dfs(n,sm):
    global result
    if n == T//2:
        start, link = 0,0
        for i in range(T):
            for j in range(i+1,T):
                if visited[i] and visited[j]:
                    start += (arr[i][j] + arr[j][i])
                elif not visited[i] and not visited[j]:
                    link += (arr[i][j] + arr[j][i])
        
        result = min(result, abs(start-link))

    for i in range(sm, T):
        if not visited[i]:
            visited[i] = True
            dfs(n+1, i+1)
            visited[i] = False

T = int(input())
arr = [list(map(int,input().split()))for _ in range(T)]
visited = [0] * (T+1)
result = 1e9
dfs(0,0)
print(result)