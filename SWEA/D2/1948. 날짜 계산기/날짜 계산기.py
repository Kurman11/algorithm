T = int(input())
m = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

for i in range(1,T+1):
    a,b,c,d = map(int,input().split())
    cnt = 0
    if a == c:
        cnt += d - b + 1

    else:
        cnt += m[a] - b + 1
        for j in range(a+1, c):
            cnt += m[j]
        
        cnt += d
    
    print(f'#{i} {cnt}')