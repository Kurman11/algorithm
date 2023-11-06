import sys
input = sys.stdin.readline

def dfs(s,e):
    visited[s] = True
    for i in graph[s]:
        if visited[i] == False:
            visited[i] = True
            e = dfs(i, e+1)
    return e


T = int(input())

for i in range(T):
    v, e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    for j in range(e):
        N, M = map(int,input().split())
        graph[N].append(M)
        graph[M].append(N)
        

    visited = [0] * (v+1)
    
    print(dfs(1,0))