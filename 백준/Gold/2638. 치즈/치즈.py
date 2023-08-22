from collections import deque

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
cnt = 0

def bfs():
    q = deque()
    q.append((0,0))
    v[0][0] == 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1,0), (1,0), (0,1), (0,-1)):
            ni , nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M :
                if v[ni][nj] == 0 and arr[ni][nj] == 0:
                    q.append((ni,nj))
                    v[ni][nj] = 1
                elif arr[ni][nj] == 1:
                    v[ni][nj] += 1


while 1:
    v = [[0] * M for _ in range(N)] 
    bfs()
    cnt += 1
    # cnt_1 = 0
    for i in range(N):
        for j in range(M):
            if v[i][j] >= 2:
                arr[i][j] = 0
    #         elif arr[i][j] == 0:
    #             cnt_1 += 1
    # if cnt_1 == (N*M):
    #     break
    cnt_1 = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                cnt_1 += 1
    if cnt_1 ==(N*M):
        break

print(cnt)