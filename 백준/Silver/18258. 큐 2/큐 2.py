import sys
from collections import deque

T = int(input())
num = deque([])

for i in range(T):
    word = sys.stdin.readline().split()
    if word[0] == 'push':
        num.append(word[1])
    elif word[0] == 'pop':
        if len(num) == 0:
            print(-1)
        else:
            print(num.popleft())
    elif word[0] == 'size':
        print(len(num))
    elif word[0] == 'empty':
        if len(num) == 0:
            print(1)
        else:
            print(0)
    elif word[0] == 'front':
        if len(num) == 0:
            print(-1)
        else:
            print(num[0])
    elif word[0] == 'back':
        if len(num) == 0:
            print(-1)
        else:
            print(num[-1])