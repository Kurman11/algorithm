T = int(input())
code = {3211:0, 2221:1, 2122:2, 1411:3, 1132:4, 1231:5, 1114:6, 1312:7, 1213:8, 3112:9}


for i in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input()))for _ in range(N)]
    lst = []
    code_lst = []
    for j in range(N):
        for k in range(M-1, -1, -1):
            if arr[j][k] == 1:
                lst.append(arr[j][k-55: k+1])
                break
            
    for l in range(0, len(lst[0]),7):
        code_lst.append(lst[0][l:l+7])

    
    code_cnt = []
    for q in code_lst:
        cnt_0 = 0
        cnt_1 = 0
        for codelst in q:
            if codelst == 0:
                if cnt_1 != 0:
                    code_cnt.append(cnt_1)
                    cnt_1 = 0            
                cnt_0 += 1
            else:
                if cnt_0 !=0:
                    code_cnt.append(cnt_0)
                    cnt_0 = 0
                cnt_1 += 1

        if cnt_0 != 0:
            code_cnt.append(cnt_0)
        elif cnt_1 != 0:
            code_cnt.append(cnt_1)

    rst = []
    for q in range(0, len(code_cnt), 4):
        cb = ''.join(map(str,code_cnt[q:q+4]))
        rst.append(int(cb))


    hol = 0
    jjak = 0
    for q in range(1, len(rst)+1):
        if q % 2 == 1:
            hol += code[rst[q-1]]
        else:
            jjak += code[rst[q-1]]
    
    sum_code = hol*3 + jjak

    if sum_code % 10 == 0:
        print(f'#{i} {hol+jjak}')
    else:
        print(f'#{i} {0}')