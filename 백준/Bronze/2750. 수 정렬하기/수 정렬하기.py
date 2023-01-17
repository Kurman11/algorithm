T = int(input())
a = []
for i in range(T):
    num = list(map(int,input().split()))
    a.append(*num)
print(*sorted(a), sep='\n')