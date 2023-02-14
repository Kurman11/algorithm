X = int(input())
N = int(input())
D = []
for i in range(N):
    a, b = list(map(int,input().split()))
    D.append(a*b)
if X == sum(D):
    print('Yes')
else:
    print('No')