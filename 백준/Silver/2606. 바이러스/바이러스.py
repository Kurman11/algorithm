T = int(input())
num = int(input())

graph = [[] for _ in range(T+1)]
visited = [False] * (T+1)

for _ in range(num):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(start):
    stack =[start]
    visited[start] = True

    while stack:
        cur = stack.pop()

        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
dfs(1)

print(visited.count(True)-1)