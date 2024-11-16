
for i in range(1, 11):
    T = int(input())
    arr = list(map(int,input().split()))
    code_num = int(input())
    code = list(map(str,input().split()))
    code_lst = [[] for _ in range(code_num)]
    check = -1

    for k in code:
        if k == 'I':
            check += 1
            continue
        code_lst[check].append(int(k))
        if check == code_num-1:
            check = -1


    for j in code_lst:
        for z in range(j[1],0,-1):
            arr.insert(j[0], j[z+1])


    print(f'#{i} {" ".join(map(str,arr[0:10]))}')
