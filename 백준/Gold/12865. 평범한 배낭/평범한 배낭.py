N, K = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(N)]
dp = [0] * (K + 1)

for i in range(N):
    w, v = lst[i]

    for j in range(K, w - 1, -1):

        if j >= w:
            dp[j] = max(dp[j], dp[j - w] + v)

print(dp[K])