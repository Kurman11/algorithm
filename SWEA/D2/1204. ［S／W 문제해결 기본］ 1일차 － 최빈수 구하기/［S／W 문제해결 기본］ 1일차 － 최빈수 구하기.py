T = int(input())

for i in range(1,T+1):
    N = int(input())
    d = dict()
    arr = list(map(int,input().split()))
    for j in arr:
        if j in d:
            d[j] += 1
        else:
            d[j] = 1
    
    max_key = max(d, key=d.get)  
    print(f'#{i} {max_key}')