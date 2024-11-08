T = int(input())

for i in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    print(f'#{i} {" ".join(map(str, arr))}')