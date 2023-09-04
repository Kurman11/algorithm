N = int(input())

arr = sorted(list(map(int,input().split())))
start , end = 0, N-1
min_sum = float('inf')
A = (0,0)

while start < end:
    sum_ = arr[start] + arr[end]

    if abs(sum_) < min_sum:
        min_sum = abs(sum_)
        A = (arr[start], arr[end])

    if sum_ < 0:
        start += 1
    else:
        end -= 1

print(A[0], A[1])