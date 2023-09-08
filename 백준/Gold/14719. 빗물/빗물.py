def asd(si,sj):
    cnt = 0
    while 1:
        sj = sj + 1
        if sj < W:
            if arr[si][sj] == 0 :
                cnt += 1
            else:
                return cnt
        else:
            return 0


H,W = map(int,input().split())

arr = [[0]*(W) for _ in range(H)]

hight = list(map(int,input().split()))

for i in range(H):
    for j in range(W):
        if hight[j] > 0:
            arr[i][j] = 1
            hight[j] -= 1

num = 0
for i in range(H):
    for j in range(W):
        if arr[i][j] == 1:
            num += asd(i,j)

print(num)