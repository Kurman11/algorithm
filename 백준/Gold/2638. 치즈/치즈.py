from collections import deque

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
cnt = 0

while True:
    q = deque()
    v = [[0 for _ in range(M)] for _ in range(N)]
    v[0][0] = 1
    q.append([0, 0])
    while q:
        x, y = q.popleft()
        for di, dj in ((-1,0), (1,0), (0,1), (0,-1)):
            nx, ny = x + di, y + dj
            if 0 <= nx < N and 0 <= ny < M and not v[nx][ny]:
                if arr[nx][ny]:
                    arr[nx][ny] += 1
                else:
                    v[nx][ny] = 1
                    q.append([nx, ny])
    
    flag = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] >=3:
                arr[i][j] = 0
            elif 0 < arr[i][j]:
                flag = 1
                arr[i][j] = 1
    cnt +=1

    if not flag:
        print(cnt)
        break