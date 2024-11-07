T = int(input())
for q in range(1, T+1):
    N,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    rst = 0

    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            
            if arr[i][j] == 0 or j == N-1:
                if cnt == K:
                    rst += 1
                cnt =0

        
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            
            if arr[j][i] == 0 or j == N-1:
                if cnt == K:
                    rst += 1
                cnt = 0

    print(f'#{q} {rst}')