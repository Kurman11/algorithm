def dfs(a):
    global visted
    visted[a] = True
    print(a, end=' ')
    for next in range(1,N+1):
        if not visted[next] and graph[a][next]:
            dfs(next)


def bfs(a):
    global q,visted
    while q:
        cur = q.pop(0)
        print(cur,end = ' ')
        for next in range(1,N+1):
            if not visted[next] and graph[cur][next]:
                visted[next] = True
                q.append(next)


# 입력 및 초기화
N, M, V = map(int,input().split())

graph = [[False] *(N+1) for _ in range(N+1)]
visted =[False] * (N+1)

# 1. graph 정보 입력
for _ in range(M):
    a, b = map(int,input().split())
    graph[a][b] = True
    graph[b][a] = True

# 2.dfs
dfs(V)
print()

# 3.bfs
visted = [False] * (N+1)

q = [V]
visted[V] = True

bfs(V)