A,B = map(int,input().split())

if A == 0:
    if B<45:
        A = 24
        C = A -1
        D = 60 - (45-B)
        print(C,D)
    elif B == 45:
        print(A,0)
    elif B > 45:
        print(A, B-45)
elif B < 45:
    C = A -1
    D = 60 - (45-B)
    print(C,D)
elif B == 45:
    print(A,0)    
elif B > 45:
    print(A, B-45)