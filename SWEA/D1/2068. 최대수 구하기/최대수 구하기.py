T = int(input())

for t in range(1,T+1):
    numbers = list(map(int,input().split()))
    a = 0
    for i in numbers:
        if i > a:
            a = i

    print(f"#{t} {a}")