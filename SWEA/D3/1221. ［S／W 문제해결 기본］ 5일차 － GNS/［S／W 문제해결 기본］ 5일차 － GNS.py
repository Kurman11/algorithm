num = {'ZRO' : 0 , 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7,'EGT':8,'NIN':9}
T = int(input())

for i in range(1,11):
    st = input()
    arr = list(map(str,input().split()))
    rst = []
    rs = []
    for j in arr:
        rst.append(num[j])
    
    rst.sort()
    
    for key, value in num.items():
        for j in rst:
            if value == j:
                rs.append(key)

    print(f'#{i}')
    print(*rs)