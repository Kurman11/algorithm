T = 10

for i in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    for _ in range(N):
        max_value = max(arr)
        min_value = min(arr)
        arr_idx_max = arr.index(max_value)    
        arr_idx_min = arr.index(min_value)    
        arr[arr_idx_max] = max_value - 1
        arr[arr_idx_min] = min_value + 1
    
    print(f'#{i} {max(arr) - min(arr)}')