N = int(input())
lst = [0] + list(map(int,input().split()))
dp = [0] * (N+1)

if max(lst[1:]) < 0:
    ans = max(lst[1:])
else:
    for i in range(1 , N+1):
        dp[i] = max(0, dp[i-1]+lst[i])
    ans = max(dp[1:])

print(ans)