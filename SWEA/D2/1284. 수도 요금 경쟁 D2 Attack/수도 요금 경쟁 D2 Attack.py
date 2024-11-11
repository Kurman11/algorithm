T = int(input())

for i in range(1, T+1):
    P,Q,R,S,W = map(int,input().split())

    first = P * W
    second = 0

    if W > R:
        second = Q + ((W-R) * S)
    else:
        if R >= W:
            second = Q

    print(f'#{i} {min(first, second)}')