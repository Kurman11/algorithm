import sys

T = int(sys.stdin.readline())
st = []
for _ in range(T):
    num = list(map(int,sys.stdin.readline().split()))
    if num[0] == 1:
        st.append(num[1])
    elif num[0] == 2:
        if len(st) == 0:
            print('-1')
        else:
            print(st.pop())
    elif num[0] == 3:
        print(len(st))
    elif num[0] == 4:
        if len(st) == 0:
            print('1')
        else:
            print('0')
    elif num[0] == 5:
        if len(st) == 0:
            print('-1')
        else:
            print(st[-1])