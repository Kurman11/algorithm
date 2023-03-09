for i in range(10):
    num = int(input())
    a,n = map(int,input().split())

    def again(a,n):
        if n == 0:
            return 1
        else:
            return a*again(a,n-1)

    print(f"#{num} {again(a, n)}")