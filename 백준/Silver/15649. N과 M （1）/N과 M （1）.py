N,M = map(int,input().split())
result = []
visited = [False for _ in range(N+1)]

def back(num):
    if num == M:
        print(' '.join(map(str,result)))
        return
    for i in range(1,N+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            back(num+1)
            visited[i] = False
            result.pop()
back(0)