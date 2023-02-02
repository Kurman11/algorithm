T = int(input())
a = ['1', '0', '0']

for t in range(1, T+1):
    v1, v2 = map(int,input().split())
    if '1' in a[v1-1]:
        a[v2-1] = a[v1-1]
        a[v1-1] = '0'
    elif '1' in a[v2-1]:
        a[v1-1] = a[v2-1]
        a[v2-1] = '0'
    elif v1 == v2:
        pass

print(a.index('1')+1)