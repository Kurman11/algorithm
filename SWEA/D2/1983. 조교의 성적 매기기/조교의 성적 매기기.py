T = int(input())
d = dict()
arr = []
rst = ['A+','A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for i in range(1, T+1):
    N, K = map(int,input().split())
    p = N // 10
    rst1 = []
    for j in rst[::-1]:
        for k in range(p):
            rst1.append(j)

    for j in range(1, N+1):
        a ,b ,c = map(int,input().split())
        d[j]=  a*0.35 + b*0.45 + c*0.2
        arr.append(a*0.35 + b*0.45 + c*0.2) 
    arr.sort()
    cnt = 0

    for z in arr:
        for key, value in d.items():
            if z == value:
                d[key] = rst1[cnt]
                cnt += 1
    print(f'#{i} {d[K]}') 