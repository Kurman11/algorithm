from collections import deque

def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    visited[si][sj] = 1
    cnt = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1,0), (1,0), (0,1), (0,-1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni <T and 0 <= nj < T and visited[ni][nj] == 0 and arr[ni][nj] == 1 :
                q.append((ni,nj))
                visited[ni][nj] = 1
                cnt += 1
    return cnt

T = int(input())
arr = [list(map(int,input())) for _ in range(T)]
visited = [[0] * T for _ in range(T)]
ans = []

for i in range(T):
    for j in range(T):
        if arr[i][j] == 1 and visited[i][j] == 0 :
            ans.append(bfs(i,j))


ans.sort()
print(len(ans), *ans, sep='\n')