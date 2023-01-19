T = int(input())
a ={}
for t in range(1,T+1):
    key ,value = input().split()
    if value == 'enter':
        a[key] = 'enter'
    else:
        del(a[key])

for key,value in sorted(a.items(),reverse=True):
    print(key)