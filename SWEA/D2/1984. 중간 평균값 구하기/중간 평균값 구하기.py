T = int(input())

for i in range(1, T+1):
    arr = list(map(int,input().split()))
    n = round((sum(arr)-max(arr)-min(arr)) / (len(arr)-2))
    print(f'#{i} {n}')