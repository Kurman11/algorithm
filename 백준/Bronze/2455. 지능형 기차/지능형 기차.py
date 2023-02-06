a = 0
b = []


for i in range(4):
    v1, v2= list(map(int,input().split()))
    a = a - v1+ v2
    b.append(a)
print(max(b))