T = int(input())

for i in range(1,T+1):
    a,b,c,d = map(int,input().split())
    h = a + c
    m = b + d

    while 1:
        if h >= 12:
            h = h - 12

        if h < 12:
            break
    while 1:
        if m >= 60:
            m = m - 60
            h += 1
        
        if m < 60:
            break
    
    print(f'#{i} {h} {m}')