T = int(input())
lst = [0] + [int(input()) for _ in range(T)]

dp = [[0]*3 for _ in range(T+1)]

for i in range(1,T+1):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) # 안 밟는 경우 1번과 2번중 큰 값을 저장
    dp[i][1] = dp[i-1][0] + lst[i] # 1번 밟는 경우 이전에 0번 밟은 값 + lst 값을 더한다.
    dp[i][2] = dp[i-1][1] + lst[i] # 2번 밟는 경우 이전에 1번 밟은 값 + lst 값을 더한다.

print(max(dp[T][1:3])) # dp리스트의 T번 값들중 1번 2번 값중 큰 값을 출력 마지막은 무조건 밟아야 하기 때문에 0번은 안한다.