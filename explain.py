# Describe how one cell of the table was computed.
def explain_cell(dp, x, y, i, j):
    if x[i - 1] == y[j - 1]:
        return (f"dp[{i}][{j}]: x[{i}]={x[i-1]} and y[{j}]={y[j-1]} MATCH -> "
                f"diagonal dp[{i-1}][{j-1}]={dp[i-1][j-1]} + 1 = {dp[i][j]}")
    top = dp[i - 1][j]
    left = dp[i][j - 1]
    source = "top" if top > left else "left"
    return (f"dp[{i}][{j}]: x[{i}]={x[i-1]} and y[{j}]={y[j-1]} no match -> "
            f"max(top={top}, left={left}) = {dp[i][j]} (from {source})")
