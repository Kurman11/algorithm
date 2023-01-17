a = []
cnt = 0
for i in range(9):
    num = list(map(int,input().split()))
    a.append(*num)
    b = sorted(a)

print(b[-1], a.index(max(a))+1, sep='\n')