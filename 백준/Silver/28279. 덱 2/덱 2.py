import sys
from collections import deque

T = int(sys.stdin.readline())
dq = deque()

for _ in range(T):
    num = list(map(int,sys.stdin.readline().split()))
    if num[0] == 1:
        dq.appendleft(num[1])
    elif num[0] == 2:
        dq.append(num[1])
    elif num[0] == 3:
        if len(dq) == 0:
            print('-1')
        else:
            print(dq.popleft())
    elif num[0] == 4:
        if len(dq) == 0:
            print('-1')
        else:
            print(dq.pop())
    elif num[0] == 5:
        print(len(dq))
    elif num[0] == 6:
        if len(dq) == 0:
            print('1')
        else:
            print('0')
    elif num[0] == 7:
        if len(dq) == 0:
            print('-1')
        else:
            print(dq[0])
    elif num[0] == 8:
        if len(dq) == 0:
            print('-1')
        else:
            print(dq[-1])