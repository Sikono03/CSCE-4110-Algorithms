def explain_cell(dp, x, y, i, j):
    if x[i - 1] == y[j - 1]:
        return (f"dp[{i}][{j}]: x[{i}]={x[i-1]} and y[{j}]={y[j-1]} MATCH -> "
                f"diagonal dp[{i-1}][{j-1}]={dp[i-1][j-1]} + 1 = {dp[i][j]}")
    top, left = dp[i - 1][j], dp[i][j - 1]
    source = "top" if top > left else "left"
    return (f"dp[{i}][{j}]: x[{i}]={x[i-1]} and y[{j}]={y[j-1]} no match -> "
            f"max(top={top}, left={left}) = {dp[i][j]} (from {source})")

def matched_positions(path):
    matches = []
    for (i1, j1), (i2, j2) in zip(path, path[1:]):
        if i2 == i1 - 1 and j2 == j1 - 1:
            matches.append((i1, j1))
    return list(reversed(matches))