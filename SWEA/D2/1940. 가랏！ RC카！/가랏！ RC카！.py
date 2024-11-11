T = int(input())

for i in range(1, T+1):
    N = int(input())
    spd = 0
    dis = 0
    for j in range(N):
        M = list(map(int,input().split()))
        if M[0] == 1:
            spd += M[1]
        elif M[0] == 2:
            spd -= M[1]
            if spd < 0:
                spd = 0
        dis += spd
    print(f'#{i} {dis}')