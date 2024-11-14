for i in range(1, 11):
    T = int(input())
    arr = [list(map(str,input())) for _ in range(8)]
    cnt = 0
    
    for j in range(8):
        for k in range(0, 8-T+1):
            check = arr[j][k:k+T]
            if check == check[::-1]:
                cnt += 1
    
    for j in range(0,8-T+1):
        for k in range(8):
            check = ''
            for z in range(T):
                check += arr[j+z][k]
            if check == check[::-1]:
                cnt += 1

    
    print(f'#{i} {cnt}')