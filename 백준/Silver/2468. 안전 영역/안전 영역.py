from collections import deque

def bfs(si,sj,h):
    q = deque()
    q.append((si,sj))
    visited[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1,0), (1,0), (0,1), (0,-1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni <T and 0 <= nj < T and visited[ni][nj] == 0 and arr[ni][nj] > h:
                q.append((ni,nj))
                visited[ni][nj] = 1


def solve(h):
    cnt = 0
    for i in range(T):
        for j in range(T):
            if arr[i][j] > h and visited[i][j] == 0:
                bfs(i,j,h)
                cnt += 1
    return cnt



T = int(input())
arr = [list(map(int,input().split())) for _ in range(T)]
ans = 0

for h in range(100):
    visited = [[0]*T for _ in range(T)]
    ans = max(ans, solve(h))

print(ans)