def gop(a, b):
    if b == M:
        return a
    return gop(a * N, b + 1)


for i in range(1, 11):
    T = int(input())
    N, M = map(int,input().split())
    print(f'#{i} {gop(N,1)}')