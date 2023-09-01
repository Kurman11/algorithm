from collections import deque

def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    cnt = 1

    while q:
        x, y = q.popleft()
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = x + dx , y + dy
            if 0<= ni < M and 0 <= nj < N and arr[ni][nj] == 0:
                arr[ni][nj] = 1
                q.append((ni,nj))
                cnt += 1
    return cnt

M,N,K = map(int,input().split())

arr = [[0]*N for _ in range(M)]
coordinate = [list(map(int,input().split())) for _ in range(K)]

while len(coordinate) != 0:
    x1, y1, x2, y2  = coordinate.pop()
    for i in range(y1,y2):
        for j in range(x1,x2):
            arr[i][j] = 1


res = []
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            arr[i][j] = 1 
            res.append(bfs(i,j))
            

print(len(res))
print(*sorted(res))