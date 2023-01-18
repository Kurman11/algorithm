T = int(input())
for t in range(1,T+1):
    num = input()
    pint = ''
    num1 = int(num[0])
    str1 = num[2::]
    for x in str1:        
        print(x*num1, end='')
    print(pint)