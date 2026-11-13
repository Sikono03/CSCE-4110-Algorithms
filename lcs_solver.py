# Build the (m + 1) x (n + 1) LCS table using bottom-up dynamic programming.
def create_table(x, y):
    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:        # match: diagonal + 1
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:                           # no match: best of top and left
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp
