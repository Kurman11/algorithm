from collections import deque

def bfs(si,sj):
    global cnt
    q = deque()
    visited[si][sj] = 1
    q.append((si,sj))
    cnt = 0
    while q:
        x,y = q.popleft()
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x + dx , y + dy
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 :
                if arr[nx][ny] == 'O':
                    visited[nx][ny] = 1
                    q.append((nx,ny))

                elif arr[nx][ny] == 'X':
                    pass

                elif arr[nx][ny] == 'P':
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    cnt += 1


N, M = map(int,input().split())
arr = [input() for _ in range(N)]
visited = [[0]*M for _ in range(N)]


for i in range(N):
    for j in range(M):
        if arr[i][j] == 'I' :
            bfs(i,j)
            cnt


if cnt == 0:
    print('TT')
else:
    print(cnt)