T = int(input())

for t in range(1,T+1):
    VPS = input()
    cnt = 0
    cnt_1 = 0
    for i in VPS:
        if i == '(':
            cnt += 1
        elif i ==')':
            cnt_1 += 1
        if cnt_1 > cnt:
            print('NO')
            break

    if cnt > cnt_1:
        print('NO')
    elif cnt == cnt_1:
        print('YES')