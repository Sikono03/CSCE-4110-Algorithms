# Trace back from dp[w][z] to recover one LCS.
def get_lcs(dp, x, y):
    i, j = len(x), len(y)
    chars = []
    path = [(i, j)]
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:  # match; keep the letter go diagonal
            chars.append(x[i - 1])
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] > dp[i][j - 1]: 
                i -= 1
            else:
                j -= 1
            path.append((i, j))
    return ''.join(reversed(chars)), path