for i in range(1, 11):
    T = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    min_s = 0
    for j in range(2, T-1):
        if arr[j] > arr[j-1] and arr[j] > arr[j-2] and arr[j] > arr[j+1] and arr[j] > arr[j+2]:
            min_s += min(arr[j] - arr[j-1], arr[j] - arr[j-2], arr[j] - arr[j+1], arr[j] - arr[j+2])
    print(f'#{i} {min_s}')