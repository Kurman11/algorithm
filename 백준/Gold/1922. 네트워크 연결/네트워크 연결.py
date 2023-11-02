import heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [ False for _ in range(n+1)]
answer = 0

for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

# 각각의 번호에 들어가는 수
# [[], [(5, 2), (4, 3)], [(5, 1), (2, 3), (7, 4)], [(4, 1), (2, 2), (6, 4), (11, 5)], [(7, 2), (6, 3), (3, 5), (8, 6)], [(11, 3), (3, 4), (8, 6)], [(8, 4), (8, 5)]]

queue = []
# 큐의 초기값
heapq.heappush(queue, (0,1))

def prim():
    global answer
    while queue:
        wei, now = heapq.heappop(queue)
        if visited[now] == False:
            visited[now] = True
            answer += wei
            for next_wei, next_node in graph[now]:
                heapq.heappush(queue, (next_wei,next_node))
    return answer

print(prim())