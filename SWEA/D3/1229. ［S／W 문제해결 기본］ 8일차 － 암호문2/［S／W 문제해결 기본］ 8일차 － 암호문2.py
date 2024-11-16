for i in range(1, 11):
    T = int(input())
    arr = list(map(int,input().split()))
    code_num = int(input())
    code = list(map(str,input().split()))
    code_lst = [[] for _ in range(code_num)]
    check = -1

    for k in code:
        if k == 'I' or k == 'D':
            check += 1
        code_lst[check].append(k)


    for j in code_lst:
        if j[0] == 'I':
            for k in range(int(j[2]),0,-1):
                arr.insert(int(j[1]),int(j[k+2]))
        elif j[0] == 'D':
            for k in range(int(j[2])):
                arr.pop(int(j[1]))

    print(f'#{i} {" ".join(map(str,arr[0:10]))}')