# Create the (w + 1) * (z + 1) LCS table using bottom-up dynamic programming.
def create_table(x, y):
    
    w, z = len(x), len(y)
    dp = [[0] * (z + 1) for _ in range(w + 1)]
    for i in range(1, w + 1):
        for j in range(1, z + 1):
            if x[i - 1] == y[j - 1]: #match
                dp[i][j] = dp[i - 1][j - 1] + 1 #diagonal + 1
            else:              # no match
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) 
    return dp