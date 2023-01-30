a = [[0 for i in range(100)]for x in range(100)]
num_list = []
z = []
for q in range(4):
    num = list(map(int,input().split()))

    for t in range(num[0],num[2]):
        for j in range(num[1],num[3]):
            a[t][j] = 1
# print(*a,sep='\n')
for k in a:
    z.append(k.count(1)) 
print(sum(z))