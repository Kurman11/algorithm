def dfs(n, rst, last_num):
    global lst
    if n == N:
        cnt_1 = 0
        cnt_2 = 0
        for i in rst:
            if  'a' in lst[i] or 'e' in lst[i] or 'i' in lst[i] or 'o' in lst[i] or 'u' in lst[i]:
                cnt_1 += 1
            else:
                cnt_2 += 1

        if cnt_1 >= 1 and cnt_2 >=2:
            result.append(rst)
            cnt_1 = 0
            cnt_2 = 0
        return 
    for i in range(M):
        if visited[i] == 0 and i > last_num: 
            visited[i] = 1
            dfs(n+1, rst+[i], i)
            visited[i] = 0

N, M = map(int,input().split())
lst = sorted(list(map(str,input().split())))
result = []
visited = [0] * (M)

dfs(0, [], -1)
cnt = 0

for i in result:
    for j in i:
        print(lst[j], end='')
    print()