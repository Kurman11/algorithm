import sys

T = int(input())
num = set(map(int, sys.stdin.readline().split()))

T_1 = int(input())
num_1 = list(map(int, sys.stdin.readline().split()))

for i in num_1:
    if i in num:
        print('1', end=' ')
    else:
        print('0', end=' ')