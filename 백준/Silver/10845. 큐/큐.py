from collections import deque
n = int(input())
dct = deque()

for i in range(n):
    arr = list(input().split())
    if arr[0] == 'push':
        dct.append(arr[1])
    elif arr[0] == 'pop':
        if len(dct) == 0:
            print(-1)
        else:
            print(dct.popleft())
    elif arr[0] == 'size':
        print(len(dct))
    elif arr[0] == 'empty':
        if len(dct) == 0:
            print(1)
        else:
            print(0)
    elif arr[0] == 'front':
        if len(dct) == 0:
            print(-1)
        else:
            print(dct[0])
    elif arr[0] == 'back':
        if len(dct) == 0:
            print(-1)
        else:
            print(dct[-1])