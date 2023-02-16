T = int(input())

for t in range(T):
    H, W, N = map(int,input().split())

    cnt = 1
    cnt_str = str(cnt)
    while 1:
        if N > H:
            N = N - H
            cnt += 1
        else:
            cnt_str = str(cnt)
            print(f'{N}{cnt_str.zfill(2)}')
            break