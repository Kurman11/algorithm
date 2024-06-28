T = int(input())
sign = list(map(str,input().split()))
visited = [0] * 10
ans = []

def check(i,j,k):
    if k == "<":
        return i < j
    else:
        return i > j

def dfs(n,sn):
    if n == T+1:
        ans.append(sn)
        return
    
    for i in range(10):
        if not visited[i]:
            if n == 0 or check(sn[-1], str(i), sign[n -1]):
                visited[i] = 1
                dfs(n+1, sn + str(i))
                visited[i] = 0

dfs(0,"")

print(ans[-1])
print(ans[0])