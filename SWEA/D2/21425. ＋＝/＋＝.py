T = int(input())

for i in range(T):
    cnt = 0
    A,B,N =map(int,input().split())
    while 1:
        cnt += 1
        if A > B:
            B += A
        else:
            A += B
        
        if (A > N or B > N):
            print(cnt)
            break