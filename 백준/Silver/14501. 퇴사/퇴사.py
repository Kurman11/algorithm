def dp(Day):
    if Day >= n:
        return 0
    if memo[Day] != -1:
        return memo[Day]

    # 선택하는 경우
    if Day + T[Day][0] <= n:
        take = T[Day][1] + dp(Day + T[Day][0])
    else:
        take = 0

    # 선택하지 않는 경우
    skip = dp(Day + 1)

    memo[Day] = max(take, skip)
    return memo[Day]

n = int(input())
T = [list(map(int, input().split())) for _ in range(n)]

# 메모이제이션을 위한 배열 초기화
memo = [-1] * n

# dp 함수를 호출하여 최대 수익 계산
max_profit = dp(0)
print(max_profit)