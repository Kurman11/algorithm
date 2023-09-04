import sys
T = int(input())
arr = sorted(list(map(int, sys.stdin.readline().split())))
S = int(input())

start, end = 0, T - 1
cnt = 0

while start < end:
    current_sum = arr[start] + arr[end]
    
    if current_sum == S:
        cnt += 1
        start += 1
        end -= 1
    elif current_sum < S:
        start += 1
    else:
        end -= 1

print(cnt)