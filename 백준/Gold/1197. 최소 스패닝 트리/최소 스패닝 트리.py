import heapq

v, e = map(int,input().split())
graph = [[] for _ in range(v+1)]
visited = [False for _ in range(v+1)]
answer = 0

for i in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

queue = []
heapq.heappush(queue,(0,1))

def prim():
    global answer
    while queue:
        wei, now = heapq.heappop(queue)
        if visited[now] == False:
            visited[now] = True
            answer += wei
            for next_wei, next_node in graph[now]:
                heapq.heappush(queue, (next_wei, next_node))
    return answer

print(prim())