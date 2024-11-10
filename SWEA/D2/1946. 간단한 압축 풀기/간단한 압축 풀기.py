T = int(input())

for i in range(1, T+1):
    N = int(input())
    c = []
    print(f'#{i}')
    for j in range(N):
        a , b = map(str,input().split())
        for j in range(int(b)):
            c.append(a)
        
    for j in range(0,len(c), 10):
        print(''.join(c[j:j+10]))