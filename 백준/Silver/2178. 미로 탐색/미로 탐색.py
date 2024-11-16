from collections import deque

def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    while q:
        ci,cj = q.popleft()

        for i in range(4):
            ni = ci + di[i]
            nj = cj + dj[i]

            if 0<=ni < N and 0<= nj < M and arr[ni][nj] == 1:
                q.append((ni,nj))
                arr[ni][nj] = arr[ci][cj] + 1
    return arr[N-1][M-1]

N, M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
print(bfs(0,0))