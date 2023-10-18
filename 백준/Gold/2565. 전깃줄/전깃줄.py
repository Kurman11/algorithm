T = int(input())

num = [list(map(int,input().split())) for _ in range(T)]
num.sort()

dp = [1] * T

for i in range(1,T):
    for j in range(0, i):
        if num[j][1] < num[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(T-max(dp))