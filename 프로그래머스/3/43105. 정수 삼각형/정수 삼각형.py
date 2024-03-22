def solution(triangle):
    # dp 테이블 초기화
    dp = [[0] * len(triangle) for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    # 거쳐간 숫자의 최댓값 구하기
    for i in range(0, len(triangle) - 1):
        for j in range(len(triangle[i])):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1])

    return max(dp[-1]) # dp 테이블의 마지막 원소들 중 최댓값 반환
