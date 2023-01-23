A,B = map(int,input().split())
num = int(input())

plus = B + num

while 1:
    if plus >= 60:
        A = A+1
        plus = plus - 60
        if A == 24:
            A = 0
    else:
        print(A,plus)
        break