
N,M = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(N)]
lst1 = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for x in range(M):
        lst[i][x] += lst1[i][x]
        
for i in lst:
    print(*i)