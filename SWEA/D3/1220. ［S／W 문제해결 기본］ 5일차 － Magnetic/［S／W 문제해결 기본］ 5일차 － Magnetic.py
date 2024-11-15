for i in range(1,11):
    T = int(input())
    arr = [list(map(int,input().split())) for _ in range(T)]
    cnt = 0
    for j in range(T):
        cnt_1 = 0
        cnt_2 = 0
        num = []
        for k in range(T):
            if arr[k][j] == 1:
                cnt_1 += 1
                num.append(1)
            if arr[k][j] == 2:
                cnt_2 += 1
                num.append(2)
        
        if cnt_1 >= 1 and cnt_2 >=1:
            while len(num) > 1 :
                if num[0] == 1 and num[-1] == 2:
                    break

                if num[0] == 2:
                    num.pop(0)

                if num[-1] == 1:
                    num.pop()

        check_1 = 0
        for k in num:
            if k == 1:
                check_1 += 1
            
            if k == 2:
                if check_1 >= 1:
                    cnt += 1
                    check_1 = 0
                
    print(f'#{i} {cnt}')   