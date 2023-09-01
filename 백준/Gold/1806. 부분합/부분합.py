N, S = map(int,input().split())
arr = list(map(int,input().split()))

start, end = 0, 0
sum_ = arr[0]
ans = 1e9

while 1:
    if sum_ < S:
        end += 1
        if end == N:
            break
        sum_ += arr[end]
    else:
        sum_ -= arr[start]
        ans = min(ans, end - start + 1)
        start += 1

if ans != 1e9:
    print(ans)
else:
    print('0')